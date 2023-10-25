#!/usr/bin/python3
"""Database Storage"""
# from sqlalchemy import
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session, query
from models.base_model import Base
from models.city import City
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User

all_classes = {
        'State': State,
        'City': City,
        'User': User,
        'Place': Place,
        'Review': Review
        }


class DBStorage:
    """This class stores the database of the project"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            cls = all_classes.values()
        else:
            if type(cls) == str:
                cls = all_classes[cls]
            cls = [cls]

        objects = {}
        for cls_ in cls:
            objs = self.__session.query(cls_).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a session."""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Removes any current session if active"""
        self.__session.close()
