from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Solicitud
from app.schemas import SolicitudCreate, SolicitudResponse, EstadoSolicitud


app = FastAPI(
    title="API de Adopciones",
    description="Servicio encargado de gestionar las solicitudes de adopción de la Fundación Huellas de Esperanza.",
    version="1.0.0"
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
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No fue posible registrar la solicitud"
        )


# Consultar todas las solicitudes
@app.get(
    "/solicitudes",
    response_model=list[SolicitudResponse]
)
def listar_solicitudes(db: Session = Depends(obtener_db)):
    return db.query(Solicitud).order_by(Solicitud.id).all()


# Consultar una solicitud por su ID
@app.get(
    "/solicitudes/{solicitud_id}",
    response_model=SolicitudResponse
)
def consultar_solicitud(
    solicitud_id: int,
    db: Session = Depends(obtener_db)
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