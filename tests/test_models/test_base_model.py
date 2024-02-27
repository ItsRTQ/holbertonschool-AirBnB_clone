#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel instances"""
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save(self):
        """Test the save method of BaseModel"""
        instance = BaseModel()
        updated_at_before = instance.updated_at
        instance.save()
        updated_at_after = instance.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertTrue(isinstance(instance_dict, dict))
        self.assertTrue("id" in instance_dict)
        self.assertTrue("created_at" in instance_dict)
        self.assertTrue("updated_at" in instance_dict)
        self.assertTrue("__class__" in instance_dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")

    def test_from_dict(self):
        """Test initialization of BaseModel from dictionary"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

if __name__ == "__main__":
    unittest.main()
