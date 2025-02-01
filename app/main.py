from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, utils
import io
import numpy as np

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.post("/autenticacion_facial/", response_model=schemas.AutenticacionFacial)
def create_autenticacion_facial(id_usuario: int = Form(...), file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    contents = file.file.read()
    encoding = utils.encode_face(io.BytesIO(contents))
    if encoding is None:
        raise HTTPException(
            status_code=400, detail="No se ha encontrado una foto en la imagen")
    return crud.create_autenticacion_facial(db=db, autenticacion=schemas.AutenticacionFacialCreate(id_usuario=id_usuario, encoding_facial=encoding.tobytes()))


@app.post("/autenticacion_facial/validar/")
def validar_autenticacion_facial(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    contents = file.file.read()
    unknown_encoding = utils.encode_face(io.BytesIO(contents))
    if unknown_encoding is None:
        raise HTTPException(
            status_code=400, detail="No se ha encontrado una foto en la imagen")

    autenticaciones = crud.get_all_autenticaciones_faciales(db)
    for autenticacion in autenticaciones:
        known_encoding = np.frombuffer(
            autenticacion.encoding_facial, dtype=np.float64)
        if utils.compare_faces(known_encoding, unknown_encoding):
            user = db.query(models.Usuario).filter(
                models.Usuario.id_usuario == autenticacion.id_usuario).first()
            return {"id_usuario": user.id_usuario}

    raise HTTPException(
        status_code=404, detail="No se ha encontrado una coincidencia")
