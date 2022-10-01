from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Depends
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import Bombilla, Habitacion, UpdateHabitacion
from sqlalchemy.orm import Session

# ShowHabitacion

router = APIRouter(
    prefix = '/Habitacion',
    tags = ["Habitacion"]
)
@router.get('')
def Obtener_Habitacion(db:Session = Depends(get_db)):
    data = db.query(models.Habitacion).all()
    return data

@router.get('/{Habitacion_Nombre}')
def Habitacion_Nombre(Habitacion_Nombre,  db:Session = Depends(get_db)):
    data = db.query(models.Habitacion).filter(models.Habitacion.Nombre == Habitacion_Nombre).first()
    print(data)
    if not data:
        return {"Respuesta":"Habitacion no encontrada"}
    return data

@router.get('/dsadad/{Habitacion_Nombre}')
def obtener_habitacionbombilla( Habitacion_Nombre:str , db:Session = Depends(get_db)):
    data = db.query(models.Bombilla).filter(models.Bombilla.Habitacion_Nombre == Habitacion_Nombre and models.Habitacion.Nombre == Habitacion_Nombre).all()
    if not data:
        return {"Respuesta":"Habitacion no encontrada"}
    return data


@router.post('')
def Crear_Habitacions(Habitacion:Habitacion, db:Session = Depends(get_db)):
    bulb = Habitacion.dict()
    nueva_Habitacion = models.Habitacion(
        Nombre =  bulb['Nombre'],
        Codigo_De_Habitacion = bulb['Codigo_De_Habitacion']
    )
    db.add(nueva_Habitacion)
    db.commit()
    return{"Respuesta":"Habitacion creada correctamente"}


@router.delete('/{Habitacion_Nombre}')
def Eliminar_Habitacion_Nombre(Habitacion_Nombre,  db:Session = Depends(get_db)):
    data = db.query(models.Habitacion).filter(models.Habitacion.Nombre == Habitacion_Nombre)
    if not data.first():
        return {"Respuesta":"Habitacion no encontrada"}
    data.delete(synchronize_session = False)
    db.commit()
    return{"Respuesta":"Habitacion eliminada correctamente"}

@router.patch('/{Habitacion_Nombre}')
def Actualizar_Habitacion(Habitacion_Nombre:str, updateHabitacion: UpdateHabitacion, db: Session = Depends(get_db)):
        data = db.query(models.Habitacion).filter(models.Habitacion.Nombre == Habitacion_Nombre)
        if not data.first():    
            return {"Respuesta":"Habitacion no encontrada"}
        data.update(updateHabitacion.dict(exclude_unset= True))
        db.commit()
        return {"Respuesta":"Habitacion Actualizada Correctamente!"}
