# ./app/crud.py

from sqlalchemy.orm import Session
from .db.models import User, Tache
from datetime import date

def create_user(db: Session, username: str, email: str, password: str):
    db_user = User(username=username, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_tache(db: Session, titre: str, date: date, description: str, etat: str, idUser: int):
    db_tache = Tache(titre=titre, date=date, description=description, etat=etat, idUser=idUser)
    db.add(db_tache)
    db.commit()
    db.refresh(db_tache)
    return db_tache

def get_taches(db: Session, tache_id: int):
    return db.query(Tache).filter(Tache.id == tache_id).first()     

def get_taches_by_user(db: Session, idUser: int):
    return db.query(Tache).filter(Tache.idUser == idUser).all()

def get_taches_by_date(db: Session, date: date):
    return db.query(Tache).filter(Tache.date == date).all()

def get_taches_by_etat(db: Session, etat: str):

    return db.query(Tache).filter(Tache.etat == etat).all()


