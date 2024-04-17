#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
and DBStorage depends on env var"""
from os import getenv

if (getenv('HBNB_TYPE_STORAGE') == 'db'):
    from models.engine import db_storage
    storage = db_storage.DBStorage()
    storage.reload()

if (getenv('HBNB_TYPE_STORAGE') == 'file'):
    from models.engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
