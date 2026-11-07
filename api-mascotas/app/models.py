from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    Text,
    DateTime,
    text
)
from app.database import Base


class Mascota(Base):
    __tablename__ = "mascotas"
    __table_args__ = {"schema": "mascotas"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(30), nullable=False)
    raza = Column(String(100), nullable=True)
    edad = Column(Integer, nullable=True)
    sexo = Column(String(20), nullable=False)
    tamano = Column(String(20), nullable=False)
    descripcion = Column(Text, nullable=True)
    foto_url = Column(Text, nullable=True)
    estado = Column(
        String(30),
        nullable=False,
        server_default=text("'disponible'")
    )
    fecha_registro = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("NOW()")
    )