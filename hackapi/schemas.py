from typing import List, Optional
from xmlrpc.client import Boolean

from pydantic import BaseModel, EmailStr, SecretStr


class Bombilla(BaseModel):
    Nombre:str
    Color:str
    Brillo:int
    Encendido_Apagado:Boolean
    Codigo_De_Bombilla:str
    Habitacion_Nombre: str
    
class UpdateBombilla(BaseModel):
    Nombre: Optional[str] = None
    Color: Optional[str] = None
    Brillo: Optional[int] = None
    Encendido_Apagado: Optional[Boolean]

class ShowBombilla(BaseModel):
    Nombre:str
    Color:str
    Brillo:int
    Encendido_Apagado:Boolean
    Codigo_De_Bombilla:str
    Habitacion_Nombre:str
    class Config():
        orm_mode = True

class Habitacion(BaseModel):
    Nombre:str
    Codigo_De_Habitacion:str

class UpdateHabitacion(BaseModel):
    Nombre:Optional[str] = None
    
class User(BaseModel):
    User_Name:str
    Email:str
    Password:str
    
    
class UserUpdate(BaseModel):
    User_Name:Optional[str]
    Email:Optional[str]
    Password:Optional[str]
    
class UserBombillasHabitaciones(BaseModel):
    Usuario_Id:int
    Codigo_Habitacion:str
    Codigo_Bombilla:str
        
class UserBombillasHabitacionesUpdate(BaseModel):
    Usuario_Id:Optional[int]
    Codigo_Habitacion:Optional[str]
    Codigo_Bombilla:Optional[str]
