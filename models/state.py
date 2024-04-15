#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models import City, storage


class State(BaseModel, Base):
    """ Rep. a state table in mysql db and inherits from SQLAlchemy
    Base class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', back_ref='state')
    if getenv('HBNB_TYPE_STORAGE' != 'db'):
        @property
        def cities(self):
            """cities getter in case file storage"""
            city_list = []
            for city in (storage.all(City).values):
                if (self.id == city.id):
                    city_list.append(city)
            return city_list
