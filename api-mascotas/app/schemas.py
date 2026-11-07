from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Especie(str, Enum):
    PERRO = "perro"
    GATO = "gato"
    OTRO = "otro"


class Sexo(str, Enum):
    MACHO = "macho"
    HEMBRA = "hembra"
    DESCONOCIDO = "desconocido"


class Tamano(str, Enum):
    PEQUENO = "pequeno"
    MEDIANO = "mediano"
    GRANDE = "grande"


class EstadoMascota(str, Enum):
    DISPONIBLE = "disponible"
    ADOPTADO = "adoptado"
    NO_DISPONIBLE = "no_disponible"


class MascotaCreate(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    especie: Especie
    raza: str | None = Field(default=None, max_length=100)
    edad: int | None = Field(default=None, ge=0)
    sexo: Sexo
    tamano: Tamano
    descripcion: str | None = None
    foto_url: str | None = None


class MascotaResponse(BaseModel):
    id: int
    nombre: str
    especie: Especie
    raza: str | None = None
    edad: int | None = None
    sexo: Sexo
    tamano: Tamano
    descripcion: str | None = None
    foto_url: str | None = None
    estado: EstadoMascota
    fecha_registro: datetime

    model_config = {"from_attributes": True}