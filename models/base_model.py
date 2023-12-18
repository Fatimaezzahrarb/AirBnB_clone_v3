#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for i, m in kwargs.items():
                if i == 'created_at' or i == 'updated_at':
                    setattr(
                        self, i, datetime.strptime(
                            m, '%Y-%m-%dT%H:%M:%S.%f'))
                elif i != '__class__':
                    setattr(self, i, m)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            time_now = datetime.utcnow()
            if 'created_at' not in kwargs:
                self.created_at = time_now
            if 'updated_at' not in kwargs:
                self.updated_at = time_now

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)
