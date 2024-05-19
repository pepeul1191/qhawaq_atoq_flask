from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from main.database import Base, Serilizable

class Level(Base, Serilizable):
  __tablename__ = 'levels'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(30), nullable=False)
  