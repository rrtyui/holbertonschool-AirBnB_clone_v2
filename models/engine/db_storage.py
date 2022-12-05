#!/usr/bin/python3
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base, BaseModel
from sqlalchemy.orm import Session

user = os.getenv("HBNB_MYSQL_USER")
pwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
db = os.getenv("HBNB_MYSQL_DB")
envv = os.getenv("HBNB_ENV")

class DBStorage:
    """
    Db
    """
    __engine = None
    __session = None

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """
        engine must be linked to the MySQL database
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)

        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        """
        obj_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                obj_dict[f"{cls}.{obj.id}"] = obj
        else:
            for clas in DBStorage.classes.values():
                for obj in self.__session.query(clas).all():
                    obj_dict[f"{type(obj).__name__}.{obj.id}"] = obj
        return obj_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reload
        """
        Base.metadata.create_all(self.__engine)
        f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(f)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute
        (self.__session"""
        self.__session.close()
