#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
=======
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
>>>>>>> 623a8c2a24154d0d1ca69a59b42d403b809fe5db

STORAGE = getenv("HBNB_TYPE_STORAGE")

<<<<<<< HEAD

class State(BaseModel, Base):
    """ State class for the states of a country """
    __tablename__ = 'states'
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='states', cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            list_city = []
            all_ins = storage.all(City)
            for value in all_ins.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city
=======
class State(BaseModel, Base):
    """Represents a state for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table states.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
>>>>>>> 623a8c2a24154d0d1ca69a59b42d403b809fe5db
