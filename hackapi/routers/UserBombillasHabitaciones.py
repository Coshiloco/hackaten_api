from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Depends
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import UserBombillasHabitaciones
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

