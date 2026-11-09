import os
import httpx
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.database import SessionLocal
from app.models import Solicitud
from app.schemas import SolicitudCreate, SolicitudResponse, EstadoSolicitud
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import (
    authenticate_admin,
    create_access_token,
    get_current_admin,
    oauth2_scheme
)


API_MASCOTAS_URL = os.getenv(
    "API_MASCOTAS_URL",
    "http://127.0.0.1:8001"
)

app = FastAPI(
    title="API de Adopciones",
    description="Servicio encargado de gestionar las solicitudes de adopción de la Fundación Huellas de Esperanza.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://huellas-de-esperanza-olive.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_admin(form_data.username, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(form_data.username)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



# Crear una sesión de base de datos por petición
def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    return {
        "mensaje": "API de Adopciones funcionando correctamente",
        "servicio": "Adopciones"
    }


@app.get("/health")
def verificar_estado():
    return {"estado": "activo"}


# Registrar una solicitud de adopción
@app.post(
    "/solicitudes",
    response_model=SolicitudResponse,
    status_code=status.HTTP_201_CREATED
)
def registrar_solicitud(
    datos: SolicitudCreate,
    db: Session = Depends(obtener_db)
):
    # 1. Consultar la mascota en la API de Mascotas
    try:
        respuesta = httpx.get(
            f"{API_MASCOTAS_URL}/mascotas/{datos.mascota_id}",
            timeout=5.0
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="No fue posible comunicarse con la API de Mascotas"
        )

    # 2. Verificar si la mascota existe
    if respuesta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="La mascota indicada no existe"
        )

    if respuesta.status_code != 200:
        raise HTTPException(
            status_code=503,
            detail="La API de Mascotas no pudo procesar la consulta"
        )

    # 3. Verificar si está disponible
    mascota = respuesta.json()

    if mascota.get("estado") != "disponible":
        raise HTTPException(
            status_code=409,
            detail="La mascota no está disponible para adopción"
        )

    # 4. Registrar la solicitud si todas las verificaciones pasan
    nueva_solicitud = Solicitud(
        mascota_id=datos.mascota_id,
        nombre_solicitante=datos.nombre_solicitante,
        correo=str(datos.correo),
        telefono=datos.telefono,
        direccion=datos.direccion,
        motivo=datos.motivo,
        estado=EstadoSolicitud.PENDIENTE.value
    )

    try:
        db.add(nueva_solicitud)
        db.commit()
        db.refresh(nueva_solicitud)
        return nueva_solicitud

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="No fue posible registrar la solicitud"
        )


# Consultar todas las solicitudes
@app.get(
    "/solicitudes",
    response_model=list[SolicitudResponse]
)
def listar_solicitudes(
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin)):
    return db.query(Solicitud).order_by(Solicitud.id).all()


# Consultar una solicitud por su ID
@app.get(
    "/solicitudes/{solicitud_id}",
    response_model=SolicitudResponse
)
def consultar_solicitud(
    solicitud_id: int,
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin)
):
    solicitud = db.query(Solicitud).filter(
        Solicitud.id == solicitud_id
    ).first()

    if solicitud is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La solicitud no fue encontrada"
        )

    return solicitud

@app.patch("/solicitudes/{solicitud_id}/aprobar", response_model=SolicitudResponse)
def aprobar_solicitud(
    solicitud_id: int,
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin),
    token: str = Depends(oauth2_scheme)
):
    # 1. Buscar la solicitud
    solicitud = db.query(Solicitud).filter(
        Solicitud.id == solicitud_id
    ).with_for_update().first()

    if solicitud is None:
        raise HTTPException(
            status_code=404,
            detail="La solicitud no fue encontrada"
        )

    # 2. Verificar que esté pendiente
    if solicitud.estado != EstadoSolicitud.PENDIENTE.value:
        raise HTTPException(
            status_code=409,
            detail="La solicitud ya fue procesada"
        )

    # 3. Solicitar a API Mascotas que adopte el animal
    try:
        respuesta = httpx.post(
            f"{API_MASCOTAS_URL}/mascotas/{solicitud.mascota_id}/adoptar",
            headers={
                "Authorization": f"Bearer {token}"
            },
            timeout=5.0
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="No fue posible comunicarse con la API de Mascotas"
        )

    # 4. Comprobar la respuesta de API Mascotas
    if respuesta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="La mascota asociada a la solicitud no existe"
        )

    if respuesta.status_code == 409:
        raise HTTPException(
            status_code=409,
            detail="La mascota ya no está disponible para adopción"
        )

    if respuesta.status_code != 200:
        raise HTTPException(
            status_code=503,
            detail="No fue posible completar la adopción en la API de Mascotas"
        )

    # 5. Actualizar la solicitud
    solicitud.estado = EstadoSolicitud.APROBADA.value
    solicitud.fecha_respuesta = datetime.now(timezone.utc)

    try:
        db.commit()
        db.refresh(solicitud)
        return solicitud

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="La mascota fue adoptada, pero no fue posible actualizar la solicitud"
        )

@app.patch("/solicitudes/{solicitud_id}/rechazar", response_model=SolicitudResponse)
def rechazar_solicitud(
    solicitud_id: int,
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin)
):
    # 1. Buscar la solicitud
    solicitud = db.query(Solicitud).filter(
        Solicitud.id == solicitud_id
    ).with_for_update().first()

    if solicitud is None:
        raise HTTPException(
            status_code=404,
            detail="La solicitud no fue encontrada"
        )

    # 2. Verificar que esté pendiente
    if solicitud.estado != EstadoSolicitud.PENDIENTE.value:
        raise HTTPException(
            status_code=409,
            detail="La solicitud ya fue procesada"
        )

    # 3. Actualizar el estado
    solicitud.estado = EstadoSolicitud.RECHAZADA.value
    solicitud.fecha_respuesta = datetime.now(timezone.utc)

    try:
        db.commit()
        db.refresh(solicitud)
        return solicitud

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="No fue posible rechazar la solicitud"
        )