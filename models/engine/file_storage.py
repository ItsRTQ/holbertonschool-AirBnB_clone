#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
import os

class FileStorage:
    """This class serializes instances to a JSON file and deserializes"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        self.targeted_dict = {}
        self.temp_key = ""
        self.objs = {}

    def all(self):
        """all, returns the objects saved in instance attribute"""

        return FileStorage.__objects

    def new(self, obj):
        """new, add obj to the instance attribute object"""

        self.temp_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objs[self.temp_key] = self.targeted_dict

    def save(self):
        """This method serialize object to json file"""
        for key, instance in FileStorage.__objects.items():
            self.objs[key] = instance.to_dict()
        self.objs[self.temp_key] = self.targeted_dict
        with open(self.__file_path, 'w') as file:
            json.dump(self.objs, file, indent=2)

    def reload(self):
        """This method de-serialize object back to instance"""

        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                temp = {}
                loaded_data = json.load(file)
                for outter_key, inner_dict in loaded_data.items():
                    temp_key = "{}.{}".format(
                        inner_dict['__class__'], inner_dict['id'])
                    temp[temp_key] = BaseModel(**inner_dict)
                FileStorage.__objects = temp
