# ./app/params.py

from pydantic import BaseModel

class UserParams(BaseModel):
    username: str
    email: str
    password: str

class GetUserParams(BaseModel):
    user_id: int

class TacheParams(BaseModel):
    titre: str
    date: str
    description: str
    etat: str
    idUser: int


class GetTachesParams(BaseModel):
    tache_id: int

class GetTacheByUserParams(BaseModel):
    idUser: int

class GetTacheByDateParams(BaseModel):
    date: str

    
