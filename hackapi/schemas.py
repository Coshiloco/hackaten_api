from typing import List, Optional
from xmlrpc.client import Boolean

from pydantic import BaseModel


class Bombilla(BaseModel):
    Nombre:str
    Color:str
    Brillo:int
    Encendido_Apagado:Boolean
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
    Habitacion_Nombre:str
    class Config():
        orm_mode = True

class Habitacion(BaseModel):
    Nombre:str
    Bombillas:list[Bombilla]

class UpdateHabitacion(BaseModel):
    Nombre:Optional[str] = None
    
class ShowHabitacion(BaseModel):
    Nombre:str
    Bombillas:list[Bombilla]


