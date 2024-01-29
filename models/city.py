#!/usr/bin/python3
'''
This module defines the City class.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

# Check the storage type
storage_type = getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    '''
    This class represents a City and inherits from BaseModel.
    '''
    __tablename__ = 'cities'

    # Define columns based on storage type
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
