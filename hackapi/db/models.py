from enum import unique

from hackapi.db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Habitacion(Base):
    __tablename__ = 'Habitacion'
    id = Column(Integer, unique = True,  autoincrement = True)
    Nombre = Column(String, primary_key = True)
    Codigo_De_Habitacion = Column(String, unique = True)
    Bombillas = relationship('Bombilla', backref = 'Habitacion', cascade = 'delete,merge')
    UserBombillasHabitaciones = relationship('UserBombillasHabitaciones', backref = 'Habitacion', cascade = 'delete,merge')

class Bombilla(Base):
    __tablename__ = 'Bombilla'
    id = Column(Integer, primary_key = True, autoincrement = True)
    Nombre = Column(String) 
    Color = Column(String)
    Brillo = Column(Integer)
    Encendido_Apagado = Column(Boolean)
    Codigo_De_Bombilla = Column(String, unique = True)
    UserBombillasHabitaciones = relationship('UserBombillasHabitaciones', backref = 'Bombilla', cascade = 'delete,merge')
    Habitacion_Nombre= Column(String,  ForeignKey("Habitacion.Nombre", ondelete = 'CASCADE'))   

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True, autoincrement = True)
    User_Name = Column(String)
    Email = Column(String)
    Password = Column(String)
    UserBombillasHabitaciones = relationship('UserBombillasHabitaciones', backref = 'Users', cascade = 'delete,merge')

class UserBombillasHabitaciones(Base):
    __tablename__ = "UserBombillasHabitaciones"
    id = Column(Integer, primary_key = True, autoincrement = True)
    Usuario_Id= Column(Integer,  ForeignKey("Users.id", ondelete = 'CASCADE'))   
    Codigo_Habitacion= Column(String,  ForeignKey("Habitacion.Codigo_De_Habitacion", ondelete = 'CASCADE'))   
    Codigo_Bombilla= Column(String,  ForeignKey("Bombilla.Codigo_De_Bombilla", ondelete = 'CASCADE'))   
