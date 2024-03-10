#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from uuid import UUID
import time

class TestBaseModel(unittest.TestCase):
    """ Unit test suite for BaseModel class """
    
    def test_id_creation(self):
        """Tests if an id is created correctly"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertTrue(isinstance(instance1.id, str))
        self.assertTrue(isinstance(instance2.id, str))
        self.assertNotEqual(instance1.id, instance2.id)

    def test_datetime_creation(self):
        """Tests if created_at, updated_at are datetime objects"""
        instance = BaseModel()
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_str_method(self):
        """Tests the __str__ method"""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_save_method(self):
        """Tests the save method"""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        time.sleep(0.01)  # Sleep for a short period to ensure a measurable time difference
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method"""
        instance = BaseModel()
        instance.name = "Test"
        instance.my_number = 30
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['name'], 'Test')
        self.assertEqual(instance_dict['my_number'], 30)
        self.assertTrue(isinstance(instance_dict['created_at'], str))
        self.assertTrue(isinstance(instance_dict['updated_at'], str))
        self.assertTrue("id" in instance_dict)

    def test_base_model_save_method(self):
        """Tests the save method of BaseModel"""
        instance = BaseModel()
        instance.save()
        key = "BaseModel." + instance.id
        with open("file.json", "r") as file:
            self.assertIn(key, file.read())

if __name__ == '__main__':
    unittest.main()
