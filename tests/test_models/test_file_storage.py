#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Defines test cases for the FileStorage class"""

    def setUp(self):
        """Set up the test case"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test case"""
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test if an instance of FileStorage is created properly"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_returns_dict(self):
        """Test if all() returns a dictionary"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test if new() properly adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test if save() properly saves objects to file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test if reload() properly loads objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
