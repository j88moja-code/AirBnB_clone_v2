#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

STORAGE = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if STORAGE == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('place', backre='cities', cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
=======
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table cities.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
>>>>>>> 623a8c2a24154d0d1ca69a59b42d403b809fe5db
