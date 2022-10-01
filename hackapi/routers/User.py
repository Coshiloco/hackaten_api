from multiprocessing import synchronize
from typing import List
from urllib import response

from fastapi import APIRouter, Depends
from hackapi.db import models
from hackapi.db.database import get_db
from hackapi.schemas import User
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/User',
    tags = ["User"]
)

@router.get('')
def Obtener_User(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data
