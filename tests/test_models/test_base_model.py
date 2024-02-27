import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def setUp(self):
        """Set up for the tests"""
        self.instance = BaseModel()

    def tearDown(self):
        """Clean up after each test"""
        del self.instance
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_instance_creation(self):
        """Test instantiation of BaseModel instance"""
        self.assertTrue(isinstance(self.instance, BaseModel))

    def test_id_unique(self):
        """Test if each instance has a unique id"""
        instance2 = BaseModel()
        self.assertNotEqual(self.instance.id, instance2.id)

    def test_datetime_created(self):
        """Test if created_at and updated_at are datetime objects"""
        self.assertTrue(isinstance(self.instance.created_at, datetime))
        self.assertTrue(isinstance(self.instance.updated_at, datetime))

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        string = "[BaseModel] ({}) {}".format(self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), string)

    def test_save_method(self):
        """Test save method updates 'updated_at'"""
    old_updated_at = self.instance.updated_at
    time.sleep(1)  # Wait for 1 second to ensure the updated_at will change
    self.instance.save()
    self.assertNotEqual(old_updated_at, self.instance.updated_at)


    def test_to_dict_method(self):
        """Test to_dict method for correct format and attributes"""
        instance_dict = self.instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], self.instance.id)
        self.assertTrue('created_at' in instance_dict)
        self.assertTrue('updated_at' in instance_dict)

if __name__ == '__main__':
    unittest.main()
