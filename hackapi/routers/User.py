from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Body, Depends
from hackapi.auth.jwt_handler import signJWT
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import User, UserLogin, UserUpdate
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
    return{"Respuesta":"Usuario creado correctamente"}

# Para logearse el usuario 

@router.post('/signup')
def user_signup(User: User = Body(default=None), db:Session = Depends(get_db)):
    bulb = User.dict()
    nuevo_User = models.User (
        User_Name =  bulb['User_Name'],
        Email = bulb['Email'],
        Password = bulb['Password']
    )
    db.add(nuevo_User)
    db.commit()
    return signJWT(User.Email)

def check_user(data: UserLogin, users_all):
    for user in users_all:
        if user.Email == data.Email  and user.Password == data.Password:
            return True
        else: return False
@router.post('/login')
def user_login(user: UserLogin, db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    if check_user(user, users_all=data):
        return signJWT(user.Email)
    else:
        return {
            "error":"Invalid login details!"
        }

@router.delete('/{User_Nombre}')
def Eliminar_User(User_Nombre,  db:Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.User_Name == User_Nombre)
    if not data.first():
        return {"Respuesta":"Usuario no encontrado"}
    data.delete(synchronize_session = False)
    db.commit()
    return{"Respuesta":"Usuario eleminado correctamente"}

@router.patch('/{User_Nombre}')
def Actualizar_User(User_Nombre:str, updateUser: UserUpdate, db: Session = Depends(get_db)):
        data = db.query(models.User).filter(models.User.User_Name == User_Nombre)
        if not data.first():    
            return {"Respuesta":"Usuario no encontrada"}
        data.update(updateUser.dict(exclude_unset= True))
        db.commit()
        return {"Respuesta":"Usuario Actualizada Correctamente!"}
