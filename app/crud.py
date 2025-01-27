from sqlalchemy.orm import Session
from . import models, schemas


def create_autenticacion_facial(db: Session, autenticacion: schemas.AutenticacionFacialCreate):
    db_autenticacion = models.AutenticacionFacial(
        id_usuario=autenticacion.id_usuario, encoding_facial=autenticacion.encoding_facial)
    db.add(db_autenticacion)
    db.commit()
    db.refresh(db_autenticacion)
    return db_autenticacion


def get_autenticacion_facial_by_usuario(db: Session, id_usuario: int):
    return db.query(models.AutenticacionFacial).filter(models.AutenticacionFacial.id_usuario == id_usuario).first()


def get_all_autenticaciones_faciales(db: Session):
    return db.query(models.AutenticacionFacial).all()
