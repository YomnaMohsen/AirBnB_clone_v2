#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
and DBStorage depends on env var"""
from os import getenv
from models.engine import file_storage
from models.engine import db_storage

if  (getenv('HBNB_TYPE_STORAGE') == 'db'):
    storage = db_storage.DBStorage()
    storage.reload()

else:
    storage = file_storage.FileStorage()
    storage.reload()
