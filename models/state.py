#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """ Rep. a state table in mysql db and inherits from SQLAlchemy
    Base class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if (getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def cities(self):
            """cities getter in case file storage"""
            city_list = []
            for city in (models.storage.all(City).values()):
                if (self.id == city.state_id):
                    city_list.append(city)
            return city_list
    else:
        cities = relationship('City', backref='state', cascade='delete')
