from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import UniqueConstraint

from . import settings


DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_movies_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Movies(DeclarativeBase):
    """Sqlalchemy movies model"""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column('title', String, unique=True)
    date = Column('date', String, nullable=True)
    duration = Column('duration', String, nullable=True)
    genre = Column('genre', String, nullable=True)
    director = Column('director', String, nullable=True)
    summary = Column('summary', String, nullable=True)