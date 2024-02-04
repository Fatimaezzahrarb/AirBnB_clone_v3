#!/usr/bin/python3
"""
Database storage engine using SQLAlchemy with a mysql+mysqldb database connection.
"""

import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Mapping class names to their corresponding model classes
class_name_to_model = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}

class DBStorage:
    """Database Storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the object"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{database}')

        # Drop all tables if in test environment
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all the objects present"""
        if not self.__session:
            self.reload()

        objects = {}
        if isinstance(cls, str):
            cls = class_name_to_model.get(cls, None)

        if cls:
            for obj in self.__session.query(cls):
                objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        else:
            for model_cls in class_name_to_model.values():
                for obj in self.__session.query(model_cls):
                    objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

        return objects

    def reload(self):
        """Reloads objects from the database"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Creates a new object"""
        self.__session.add(obj)

    def save(self):
        """Saves the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object"""
        if not self.__session:
            self.reload()

        if obj:
            self.__session.delete(obj)

    def close(self):
        """Dispose of the current session if active"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieve an object by class name and ID"""
        if cls is not None and isinstance(cls, str) and id is not None and isinstance(id, str) and cls in class_name_to_model:
            cls = class_name_to_model[cls]
            result = self.__session.query(cls).filter(cls.id == id).first()
            return result
        else:
            return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        total = 0
        if isinstance(cls, str) and cls in class_name_to_model:
            cls = class_name_to_model[cls]
            total = self.__session.query(cls).count()
        elif cls is None:
            for model_cls in class_name_to_model.values():
                total += self.__session.query(model_cls).count()
        return total
