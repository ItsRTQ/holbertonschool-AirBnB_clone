#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
import os

class FileStorage:
    """This class serializes instances to a JSON file and deserializes"""

    __file_path = "file.json"
    __object = {}

    def all(self):
        """all, returns the objects saved in instance attribute"""

        return self.__object

    def new(self, obj):
        """new, add obj to the instance attribute object"""

        temp = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__object[temp] = obj.to_dict()

    def save(self):
        """This method serialize object to json file"""

        with open(self.__file_path, 'w') as file:
            json.dump(self.__object, file, indent=2)

    def reload(self):
        """This method de-serialize object back to instance"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__object = json.load(file)
