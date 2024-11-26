import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__="planet"

    id = Column(Integer, primary_key=True)
    name=Column(String(200))
    population=Column(Integer)
    weather=Column(String(50),nullable=False)

class Character(Base):
    __tablename__="character"

    id = Column(Integer,primary_key=True)
    name=Column(String(200))
    age=Column(Integer)
    zodiac=Column(String(100))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
#    favorite=relationship(Favorite)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    

    def to_dict(self):
        return {}
    
class Favorite(Base):
    __tablename__="favorite"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    character_id=Column(ForeignKey('character.id'))
    character=relationship(Character)
    planet_id=Column(ForeignKey('planet.id'))
    planet=relationship(Planet)  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')