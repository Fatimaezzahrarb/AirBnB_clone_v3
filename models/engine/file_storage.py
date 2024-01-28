#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes them back to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects, or a dictionary
        of objects of a specific class if cls is provided.
        """
        if cls is not None:
            new_dict = {
                key: value
                for key, value in self.__objects.items()
                if cls == value.__class__ or cls == value.__class__.__name__
            }
            return new_dict
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary with
        the key "<obj class name>.id".
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects dictionary to the JSON file
        (located at __file_path).
        """
        json_objects = {
            key: self.__objects[key].to_dict() for key in self.__objects
        }
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file (located at __file_path)
        back to the __objects dictionary.
        """
        try:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for key in json_data:
                class_name = json_data[key]["__class__"]
                obj = classes[class_name](**json_data[key])
                self.__objects[key] = obj
        except Exception:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from the __objects dictionary if it exists.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """
        Calls the reload() method to deserialize the JSON
        file and load objects into memory.
        """
        self.reload()
