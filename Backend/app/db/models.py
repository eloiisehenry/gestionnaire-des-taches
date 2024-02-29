# ./app/db/models.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    taches = relationship("Tache", back_populates="user")

class Tache(Base):
    __tablename__ = "taches"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255))
    date = Column(Date)
    description = Column(String(255))
    etat = Column(String(255))
    idUser = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="taches")
