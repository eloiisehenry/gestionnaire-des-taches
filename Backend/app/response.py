# ./app/response.py

from pydantic import BaseModel
from datetime import date

class IndexResponse(BaseModel):
    msg: str

class UserResponse(BaseModel):
    email: str
    name: str

class TacheResponse(BaseModel):
    titre: str
    date: date
    description: str
    etat: str

class TacheByUserResponse(BaseModel):
    titre: str
    date: date
    description: str
    etat: str
    user: str

class TacheByDateResponse(BaseModel):
    titre: str
    date: date
    description: str
    etat: str
    user: str
