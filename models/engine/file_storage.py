#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
import os

class FileStorage:
    """This class serializes instances to a JSON file and deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all, returns the objects saved in instance attribute"""

        return self.__objects

    def new(self, obj):
        """new, add obj to the instance attribute object"""

        temp = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[temp] = obj.to_dict()

    def save(self):
        """This method serialize object to json file"""

        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """This method de-serialize object back to instance"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                self.__objects = {}
                for key, value in loaded_data.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj_instance = class_(**value)
                    self.__objects[key] = obj_instance
