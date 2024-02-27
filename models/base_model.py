#!/usr/bin/python3
"""
BaseModel module: Defines the BaseModel class
"""
from models import storage
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the instance's updated_at attribute
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's __dict__
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
