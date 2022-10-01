'''
La funcion de este archivo es comprobar is 
la peticion o request esta autorizada 
o no para asi verificar una ruta protegida
'''

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .jwt_handler import decodeJWT

class jwtBearer(HTTPBearer):
  def __init__(self, auto_Error : bool = True):
    super(jwtBearer, self).__init__(auto_error=auto_Error)
  
  async def __call__(self, request: Request):
    credentials : HTTPAuthorizationCredentials = await super(jwtBearer,
    self).__call__(request=request)
    if credentials:
      if not credentials.schema == "Bearer":
        raise HTTPException(status_code=403, detail="Invalid or expire token")
      return credentials.credentials
    else:
      raise HTTPException(status_code=403, detail="Invalid or expire token")
  
  def verify_jwt(self, jwtoken: str):
    isTokenValid : bool = False
    payload = decodeJWT(jwtoken)
    if payload:
      isTokenValid = True
    return isTokenValid