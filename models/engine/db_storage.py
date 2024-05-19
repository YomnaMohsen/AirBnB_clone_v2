#!/usr/bin/python3
"""new DBstorage engine module"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Dbstorage class"""
    __engine = None
    __session = None
    __classes_dict = {"User": User, "State": State,
                      "Review": Review, "Place": Place,
                      "Amenity": Amenity, "City": City}

    def __init__(self):
        """Initilaze dbstorage module"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                                 getenv('HBNB_MYSQL_PWD'),
                                                 getenv('HBNB_MYSQL_HOST'),
                                                 getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if (getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return dictionary of objects in current session
        based on cls (class name)"""
        obj_dict = {}
        if (cls is not None):
            for inst in (self.__session.query(cls).all()):
                name = inst.__class__.__name__
                obj_dict[name + "." + inst.id] = inst
        else:
            for class_obj in DBStorage.__classes_dict.values():
                for inst in (self.__session.query(class_obj).all()):
                    # try cls.__class__.__name__
                    name = inst.__class__.__name__
                    obj_dict[name + "." + inst.id] = inst

        return (obj_dict)

    def new(self, obj):
        """add new obj in db session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session
        obj if not None"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close method"""
        self.__session.close()
