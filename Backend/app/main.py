# ./app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine
from app.db import models
from app.response import IndexResponse, UserResponse, TacheResponse
from app.params import UserParams, GetUserParams, TacheParams, GetTachesParams, GetTacheByUserParams, GetTacheByDateParams
from app import crud


app = FastAPI()

# Configure database
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Additional endpoint for the main page
@app.get("/", response_model=IndexResponse)
def index():
    return {"msg": "Welcome to the FastAPI gestionnaire des taches app!"}

# Create a user
@app.post("/user/create/")
def create_user(user: UserParams, db: Session = Depends(get_db)):
    return crud.create_user(db=db, username=user.username, email=user.email, password=user.password)

@app.get("/user/get/",response_model=UserResponse)
def get_user(user: GetUserParams,db: Session = Depends(get_db)):
    user = crud.get_user(db=db,user_id = user.user_id )
    return {
        'email': user.email,
        'name': user.username
    }

@app.post("/tache/create/")
def create_tache(tache: TacheParams, db: Session = Depends(get_db)):
    return crud.create_tache(db=db, titre=tache.titre, date=tache.date, description=tache.description, etat=tache.etat, idUser=tache.idUser)

@app.get("/tache/get/",response_model=TacheResponse)
def get_tache(tache: GetTachesParams,db: Session = Depends(get_db)):
    tache = crud.get_tache(db=db,tache_id = tache.tache_id )
    return {
        'titre': tache.titre,
        'date': tache.date,
        'description': tache.description,
        'etat': tache.etat
    }

@app.get("/tache/getByUser/",response_model=TacheResponse)
def get_tache_by_user(tache: GetTacheByUserParams,db: Session = Depends(get_db)):
    taches = crud.get_tache_by_user(db=db,idUser = tache.idUser )
    return taches

@app.get("/tache/getByDate/",response_model=TacheResponse)
def get_tache_by_date(tache: GetTacheByDateParams,db: Session = Depends(get_db)):
    taches = crud.get_tache_by_date(db=db,date = tache.date )
    return taches

