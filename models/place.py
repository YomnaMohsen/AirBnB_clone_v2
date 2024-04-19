#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Table, Float
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('user', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), 
           primary_key=True, nullable = False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), 
           primary_key=True, nullable = False))

class Place(BaseModel, Base):
    """ Rep. a place table in mysql db and inherits from SQLAlchemy
    Base class"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship ('Amenity', backref='place',
                                  secondary=place_amenity, viewonly= False)
    else:
        @property
        def reviews(self):
            """reviews getter in case file storage"""
            review_list = []
            for rev in (models.storage.all(Review).values):
                if (self.id == rev.place_id):
                    review_list.append(rev)
            return review_list
        
        @property
        def amenities(self):
            """amenities getter in case file storage"""
            ament_list = []
            for amen in (models.storage.all(Amenity).values):
                if amen.id in self.amenity_ids:
                    ament_list.append(amen)
                
            return ament_list    

        @amenities.setter
        def amenities(self, amenity):
            """Setter for linked aminities"""
            self.amenity_ids = []
            if (isinstance(amenity, Amenity)):
                self.amenity_ids.append(amenity.id)