from pydantic import BaseModel


class AutenticacionFacialBase(BaseModel):
    id_usuario: int


class AutenticacionFacialCreate(AutenticacionFacialBase):
    encoding_facial: bytes


class AutenticacionFacial(AutenticacionFacialBase):
    id_autenticacion: int

    class Config:
        from_attributes = True
