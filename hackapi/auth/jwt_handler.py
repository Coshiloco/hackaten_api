'''
This files is reponsible for signing, enconding
decoding and returning JWTs-


'''
#  Para la fecha de expiracion y de mas
import time

# Para encondear y decaodear los jwts
import jwt
# Para almacenar los parametros
from decouple import config

JWT_SECRET = config("secret")
JSWT_ALGORITHM = config("algorithm")

#  Returned the genrates tokens JWT in string
def token_reponse(token: str):
  return {
    "access token": token
  }
  
def signJWT(userID: str):
  payload = {
    "userID": userID,
    "expiry": time.time() + 600
  }
  token = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JSWT_ALGORITHM)
  return token_reponse(token=token)

def decodeJWT(token: str):
  try:
    decode_token = jwt.decode(token, JWT_SECRET, algorithm=JSWT_ALGORITHM)
    return decode_token if decode_token['expires'] >= time.time() else None 
  except:
    return {}
    
    