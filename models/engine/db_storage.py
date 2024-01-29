#!/usr/bin/python3
"""
This module contains the DBStorage class.
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

classes = {
    "State": State,
    "City": City,
    "User": User,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity
}


class DBStorage:
    """
    This class handles database storage using SQLAlchemy.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage instance.
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database),
            pool_pre_ping=True
        )

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or a
        dictionary of objects of a specific class.
        """
        db_objects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    db_objects[key] = val
            elif cls.__name__ in classes:
                for obj in self.__session.query(cls).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    db_objects[key] = val
        else:
            for class_name, class_obj in classes.items():
                for obj in self.__session.query(class_obj).all():
                    key = str(class_obj.__name__) + "." + str(obj.id)
                    val = obj
                    db_objects[key] = val
        return db_objects

    def new(self, obj):
        """
        Adds an object to the current database session.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.close()
