#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
import os

class FileStorage:
    """This class serializes instances to a JSON file and deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all, returns the objects saved in storage"""

        return self.__objects

    def new(self, obj):
        """new, add obj to the instance attribute object
            Adds a new instance to storage dict
        """

        temp = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[temp] = obj
 
    def save(self):
        """This method serialize object to json file
            Save the data into a json file in a dict of dicts format
        """
        prep_data = {}
        for key, instans in FileStorage.__objects.items():
            if not isinstance(FileStorage.__objects[key], dict):
                prep_data[key] = FileStorage.__objects[key].to_dict()
            else:
                prep_data[key] = FileStorage.__objects[key]
        with open(self.__file_path, 'w') as file:
            json.dump(prep_data, file, indent=2)

    def reload(self):
        """This method de-serialize object back to instance
            Verify if the file exist 
                if it exist it retrive the data into storage
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
