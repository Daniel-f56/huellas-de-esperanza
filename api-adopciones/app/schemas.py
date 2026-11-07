
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


# Estados permitidos para las solicitudes
class EstadoSolicitud(str, Enum):
    PENDIENTE = "pendiente"
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"


# Datos que recibimos al registrar una solicitud
class SolicitudCreate(BaseModel):
    mascota_id: int = Field(gt=0)

    nombre_solicitante: str = Field(min_length=3, max_length=150)

    correo: EmailStr

    telefono: str = Field(min_length=7, max_length=30)

    direccion: str = Field(min_length=5, max_length=250)

    motivo: str = Field(min_length=10)


# Datos que devolverá la API al consultar una solicitud
class SolicitudResponse(BaseModel):
    id: int
    mascota_id: int
    nombre_solicitante: str
    correo: str
    telefono: str
    direccion: str
    motivo: str
    estado: EstadoSolicitud
    fecha_solicitud: datetime
    fecha_respuesta: datetime | None = None

    model_config = {
        "from_attributes": True
    }
