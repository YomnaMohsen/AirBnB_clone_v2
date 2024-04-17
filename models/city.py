#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

places = relationship('City', backref='cities', cascade='delete')


class City(BaseModel, Base):
    """ Rep. a city table im mysql db and inherits from SQLAlchemy
    Base class"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
