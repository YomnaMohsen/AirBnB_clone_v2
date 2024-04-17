#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Rep. a review table in mysql db and inherits from SQLAlchemy
    Base class"""
