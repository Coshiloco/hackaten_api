from hackapi.db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Habitacion(Base):
    __tablename__ = 'Habitacion'
    id = Column(Integer, autoincrement = True)
    Nombre = Column(String, primary_key = True)
    Bombillas = [relationship('Bombilla', backref = 'Habitacion', cascade = 'delete,merge')]


class Bombilla(Base):
    __tablename__ = 'Bombilla'
    id = Column(Integer, primary_key = True, autoincrement = True)
    Nombre = Column(String) 
    Color = Column(String)
    Brillo = Column(Integer)
    Encendido_Apagado = Column(Boolean)
    Habitacion_Nombre= Column(String,  ForeignKey("Habitacion.Nombre", ondelete = 'CASCADE'))   

