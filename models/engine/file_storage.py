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

    def all(self):
        """all, returns the objects saved in instance attribute"""

        return self.__objects

    def new(self, obj):
        """new, add obj to the instance attribute object"""

        self.temp_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[self.temp_key] = self.targeted_dict

    def save(self):
        """This method serialize object to json file"""

        FileStorage.__objects[self.temp_key] = self.targeted_dict
        with open(self.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file, indent=2)

    def reload(self):
        """This method de-serialize object back to instance"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                FileStorage.__objects = loaded_data
