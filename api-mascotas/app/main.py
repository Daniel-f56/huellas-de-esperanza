from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import SessionLocal
from app.models import Mascota
from app.schemas import (
    MascotaCreate,
    MascotaResponse,
    EstadoMascota
)
from app.auth import get_current_admin

app = FastAPI(
    title="API de Mascotas",
    description="Servicio encargado de gestionar las mascotas disponibles para adopción de la Fundación Huellas de Esperanza.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://huellas-de-esperanza-olive.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        "mensaje": "API de Mascotas funcionando correctamente",
        "servicio": "Mascotas"
    }


@app.get("/health")
def verificar_estado():
    return {"estado": "activo"}


# Registrar una mascota
@app.post(
    "/mascotas",
    response_model=MascotaResponse,
    status_code=status.HTTP_201_CREATED
)
def registrar_mascota(
    datos: MascotaCreate,
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin)
):
    nueva_mascota = Mascota(
        nombre=datos.nombre,
        especie=datos.especie.value,
        raza=datos.raza,
        edad=datos.edad,
        sexo=datos.sexo.value,
        tamano=datos.tamano.value,
        descripcion=datos.descripcion,
        foto_url=datos.foto_url,
        estado=EstadoMascota.DISPONIBLE.value
    )

    try:
        db.add(nueva_mascota)
        db.commit()
        db.refresh(nueva_mascota)
        return nueva_mascota

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No fue posible registrar la mascota"
        )


# Consultar todas las mascotas
@app.get("/mascotas", response_model=list[MascotaResponse])
def listar_mascotas(db: Session = Depends(obtener_db)):
    return db.query(Mascota).order_by(Mascota.id).all()


# Consultar una mascota por su ID
@app.get("/mascotas/{mascota_id}", response_model=MascotaResponse)
def consultar_mascota(
    mascota_id: int,
    db: Session = Depends(obtener_db)
):
    mascota = db.query(Mascota).filter(
        Mascota.id == mascota_id
    ).first()

    if mascota is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La mascota no fue encontrada"
        )

    return mascota


# Cambiar el estado de una mascota
@app.patch(
    "/mascotas/{mascota_id}/estado",
    response_model=MascotaResponse
)
def cambiar_estado_mascota(
    mascota_id: int,
    nuevo_estado: EstadoMascota,
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin)
):
    mascota = db.query(Mascota).filter(
        Mascota.id == mascota_id
    ).with_for_update().first()

    if mascota is None:
        raise HTTPException(
            status_code=404,
            detail="La mascota no fue encontrada"
    )

    # Impedir que una mascota adoptada vuelva a otro estado
    if (
            mascota.estado == EstadoMascota.ADOPTADO.value
    and nuevo_estado != EstadoMascota.ADOPTADO
    ):
        
        raise HTTPException(
            status_code=409,
            detail="No se puede modificar el estado de una mascota que ya fue adoptada"
        )

    mascota.estado = nuevo_estado.value

    try:
        db.commit()
        db.refresh(mascota)
        return mascota

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No fue posible actualizar el estado de la mascota"
        )


# Adoptar una mascota
@app.post(
    "/mascotas/{mascota_id}/adoptar",
    response_model=MascotaResponse
)
def adoptar_mascota(
    mascota_id: int,
    db: Session = Depends(obtener_db),
    admin: str = Depends(get_current_admin)
):
    mascota = db.query(Mascota).filter(
        Mascota.id == mascota_id
    ).with_for_update().first()

    if mascota is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La mascota no fue encontrada"
        )

    if mascota.estado != EstadoMascota.DISPONIBLE.value:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="La mascota no está disponible para adopción"
        )

    mascota.estado = EstadoMascota.ADOPTADO.value

    try:
        db.commit()
        db.refresh(mascota)
        return mascota

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No fue posible completar la adopción"
        )