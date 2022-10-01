from http.client import UNPROCESSABLE_ENTITY
from operator import index
from xmlrpc.client import Boolean

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from hackapi.db.database import Base, engine
from hackapi.routers import (Bombilla, Habitacion, User,
                             UserBombillasHabitaciones)


def create_tables():
    Base.metadata.create_all(bind=engine)
    

create_tables()
app = FastAPI()

app.include_router(Bombilla.router)
app.include_router(Habitacion.router)
app.include_router(User.router)
app.include_router(UserBombillasHabitaciones.router)
