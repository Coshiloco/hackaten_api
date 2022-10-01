from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Depends
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import (UserBombillasHabitaciones,
                             UserBombillasHabitacionesUpdate)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/UserBombillasHabitaciones',
    tags = ["UserBombillasHabitaciones"]
)



@router.get('')
def Obtener_Users(db:Session = Depends(get_db)):
    data = db.query(models.UserBombillasHabitaciones).all()
    return data


@router.post('')
def Crear_Users(UserBombillasHabitaciones:UserBombillasHabitaciones, db:Session = Depends(get_db)):
    bulb = UserBombillasHabitaciones.dict()
    nuevo_UserBombillasHabitaciones = models.UserBombillasHabitaciones (
        Usuario_Id =  bulb['Usuario_Id'],
        Codigo_Habitacion = bulb['Codigo_Habitacion'],
        Codigo_Bombilla = bulb['Codigo_Bombilla'],
    )
    db.add(nuevo_UserBombillasHabitaciones)
    db.commit()
    return{"Respuesta":"Habitacion creada correctamente"}
    
    
@router.delete('/{Codigo_Habitacion}')
def Eliminar_User(Codigo_Habitacion,  db:Session = Depends(get_db)):
    data = db.query(models.UserBombillasHabitaciones).filter(models.UserBombillasHabitaciones.Codigo_Habitacion == Codigo_Habitacion)
    if not data.first():
        return {"Respuesta":"Usuario no encontrado"}
    data.delete(synchronize_session = False)
    db.commit()
    return{"Respuesta":"Usuario eleminado correctamente"}

@router.patch('/{Codigo_Habitacion}')
def Actualizar_User(Codigo_Habitacion:str, UserBombillasHabitacionesUpdate: UserBombillasHabitacionesUpdate, db: Session = Depends(get_db)):
        data = db.query(models.UserBombillasHabitacionesUpdate).filter(models.UserBombillasHabitacionesUpdate.Codigo_Habitacion == Codigo_Habitacion)
        if not data.first():    
            return {"Respuesta":"Usuario no encontrada"}
        data.update(UserBombillasHabitacionesUpdate.dict(exclude_unset= True))
        db.commit()
        return {"Respuesta":"Usuario Actualizada Correctamente!"}
        
@router.delete('/{Codigo_Bombilla}')
def Eliminar_User(Codigo_Bombilla,  db:Session = Depends(get_db)):
    data = db.query(models.UserBombillasHabitaciones).filter(models.UserBombillasHabitaciones.Codigo_Bombilla == Codigo_Bombilla)
    if not data.first():
        return {"Respuesta":"Usuario no encontrado"}
    data.delete(synchronize_session = False)
    db.commit()
    return{"Respuesta":"Usuario eleminado correctamente"}

@router.patch('/{Codigo_Bombilla}')
def Actualizar_User(Codigo_Bombilla:str, UserBombillasHabitacionesUpdate: UserBombillasHabitacionesUpdate, db: Session = Depends(get_db)):
        data = db.query(models.UserBombillasHabitacionesUpdate).filter(models.UserBombillasHabitacionesUpdate.Codigo_Bombilla == Codigo_Bombilla)
        if not data.first():    
            return {"Respuesta":"Usuario no encontrada"}
        data.update(UserBombillasHabitacionesUpdate.dict(exclude_unset= True))
        db.commit()
        return {"Respuesta":"Usuario Actualizada Correctamente!"}

