from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    DateTime,
    text
)

from app.database import Base


class Solicitud(Base):
    __tablename__ = "solicitudes"
    __table_args__ = {"schema": "adopciones"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    mascota_id = Column(BigInteger, nullable=False)

    nombre_solicitante = Column(String(150), nullable=False)
    correo = Column(String(150), nullable=False)
    telefono = Column(String(30), nullable=False)
    direccion = Column(String(250), nullable=False)
    motivo = Column(Text, nullable=False)

    estado = Column(
        String(20),
        nullable=False,
        server_default=text("'pendiente'")
    )

    fecha_solicitud = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("NOW()")
    )

    fecha_respuesta = Column(
        DateTime(timezone=True),
        nullable=True
    )