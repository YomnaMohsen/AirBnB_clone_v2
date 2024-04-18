#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review


class Place(BaseModel, Base):
    """ Rep. a place table in mysql db and inherits from SQLAlchemy
    Base class"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship('Review', backref='place', cascade='delete')
    else:
        @property
        def reviews(self):
            """reviews getter in case file storage"""
            review_list = []
            for rev in (models.storage.all(Review).values):
                if (self.id == rev.id):
                    review_list.append(rev)
            return review_list
