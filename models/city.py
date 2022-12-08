#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
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
