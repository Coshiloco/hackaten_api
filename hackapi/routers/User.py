from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Depends
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import User, UserUpdate
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/Users',
    tags = ["Users"]
)

@router.get('')
def Obtener_Users(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data


@router.post('')
def Crear_Users(User:User, db:Session = Depends(get_db)):
    bulb = User.dict()
    nuevo_User = models.User (
        User_Name =  bulb['User_Name'],
        Email = bulb['Email'],
        Password = bulb['Password']
    )
    db.add(nuevo_User)
    db.commit()
    return{"Respuesta":"Habitacion creada correctamente"}
