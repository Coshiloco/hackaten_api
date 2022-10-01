from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Depends
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import Bombilla, ShowBombilla, UpdateBombilla
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/bombilla',
    tags = ["Bombilla"]
)

@router.get('', response_model = List[ShowBombilla])
def Obtener_Bombillas(db:Session = Depends(get_db)):
    data = db.query(models.Bombilla).all()
    return data

@router.get('/{bombilla_Nombre}', response_model = ShowBombilla)
def Bombilla_Nombre(bombilla_Nombre,  db:Session = Depends(get_db)):
    data = db.query(models.Bombilla).filter(models.Bombilla.id == bombilla_Nombre).first()
    if not data:
        return {"Respuesta":"Bombilla no encontrada"}
    return data

@router.post('')
def Crear_Bombillas(bombilla:Bombilla, db:Session = Depends(get_db)):
    bulb = bombilla.dict()
    nueva_bombilla = models.Bombilla(
        Nombre =  bulb['Nombre'],
        Color =  bulb[ 'Color'],
        Brillo = bulb['Brillo'],
        Encendido_Apagado = bulb['Encendido_Apagado'],
        Codigo_De_Bombilla = bulb['Codigo_De_Bombilla'],
        Habitacion_Nombre = bulb['Habitacion_Nombre']
    )
    db.add(nueva_bombilla)
    db.commit()
    return{"Respuesta":"Bombilla creada correctamente"}


@router.delete('/{bombilla_id}')
def Eliminar_Bombilla_id(bombilla_id,  db:Session = Depends(get_db)):
    data = db.query(models.Bombilla).filter(models.Bombilla.id == bombilla_id)
    if not data.first():
        return {"Respuesta":"Bombilla no encontrada"}
    data.delete(synchronize_session = False)
    db.commit()
    return{"Respuesta":"Bombilla eliminada correctamente"}

@router.patch('/{bombilla_id}')
def Actualizar_Bombilla(user_id :int, updatebombilla: UpdateBombilla, db: Session = Depends(get_db)):
        data = db.query(models.Bombilla).filter(models.Bombilla.id == user_id)
        if not data.first():    
            return {"Respuesta":"Bombilla no encontrada"}
        data.update(updatebombilla.dict(exclude_unset= True))
        db.commit()
        return {"Respuesta":"Bombilla Actualizada Correctamente!"}
