import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    rotation_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(Integer)
    terrain = Column(String(250))
    surface_water = Column(String(250))
    language = Column(String(250))


    def to_dict(self):
        return{}

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    eye_colors = Column(String(250))
    homeplanet_id = Column(String(250), ForeignKey('planets.id'))
    homeplanet = relationship(Planets, primaryjoin=homeplanet_id == Planets.id)
    language = Column(String(250))


    def to_dict(self):
        return{}

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(50))
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species, primaryjoin=species_id == Species.id)
    homeplanet_id =  Column(Integer, ForeignKey('planets.id'))
    homeplanet = relationship(Planets, primaryjoin=homeplanet_id == Planets.id)
    starship_id = Column(Integer, ForeignKey('vehicles.id'))
    starship = relationship('Vehicles', back_populates='id')
   
    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250))
    manufacturer  = Column(String(250))
    cost_in_credits = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    pilot_id = Column(Integer, ForeignKey('characters.id'))
    pilot = relationship(Characters, primaryjoin=pilot_id == Characters.id)
    copilot_id = Column(Integer, ForeignKey('characters.id'))
    copilot = relationship(Characters, primaryjoin=copilot_id == Characters.id)

    def to_dict(self):
        return{}

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites_by_user.id'))
    favorites = relationship("Favorites_by_user", back_populates="id")
    date_at = Column(DateTime, default=datetime.datetime.now())

    def to_dict(self):
        return{}


class Favorites_by_user(Base):
    __tablename__ = 'favorites_by_user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users, primaryjoin=user_id == Users.id)
    characters_id = Column(Integer, ForeignKey('characters.id')) 
    characters = relationship(Characters, primaryjoin=characters_id == Characters.id)
    planets_id = Column(Integer, ForeignKey('planets.id')) 
    planets = relationship(Planets, primaryjoin=planets_id == Planets.id)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles, primaryjoin=vehicles_id == Vehicles.id)
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species, primaryjoin=species_id == Species.id)

    def to_dict(self):
        return{}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')