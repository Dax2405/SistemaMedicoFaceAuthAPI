from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    tipo_usuario = Column(String(10), nullable=False)
    estado = Column(String(1), default='A')
    fecha_crea = Column(TIMESTAMP, server_default=func.now())
    fecha_modifica = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())


class AutenticacionFacial(Base):
    __tablename__ = "autenticacion_facial"
    id_autenticacion = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey(
        "usuario.id_usuario"), nullable=False)
    encoding_facial = Column(BLOB, nullable=False)
    fecha_crea = Column(TIMESTAMP, server_default=func.now())
    usuario = relationship("Usuario")
