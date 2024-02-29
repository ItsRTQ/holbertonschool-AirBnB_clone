#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State


class FileStorage:
    """This class serializes instances to a JSON file and deserializes"""
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def classes():
        """Returns a dictionary of all valid classes"""

        return {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "State": State,
            "Review": Review
        }

    def all(self):
        """Returns the objects saved in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new instance to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        prep_data = {key: obj.to_dict() for key,
                     obj in FileStorage.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(prep_data, file, indent=2)

    def reload(self):
        """Deserializes the JSON file to objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for obj_id, obj_data in data.items():
                    class_name = obj_data['__class__']
                    if class_name in FileStorage.classes():
                        self.new(FileStorage.classes()[class_name](**obj_data))

    def reset_filestorage(self):
        """Resets file storage"""
        FileStorage.__objects = {}
