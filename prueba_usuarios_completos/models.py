# models.py

from sqlalchemy import Column, Date, Integer, String
from database import Base



class Usuario(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    apellidos = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    fecha_nacimiento = Column(Date, index=True)
