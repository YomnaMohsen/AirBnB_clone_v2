#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
and DBStorage depends on env var"""
from models.engine.file_storage import FileStorage
#  from models.engine.db_storage import DBStorage
# from os import getenv

# if (getenv('HBNB_TYPE_STORAGE') == 'db'):
# storage = DBStorage()

# if (getenv('HBNB_TYPE_STORAGE') == 'file'):
storage = FileStorage()
storage.reload()
