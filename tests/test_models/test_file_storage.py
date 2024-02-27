import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up method to start each test"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.obj = BaseModel()

    def tearDown(self):
        """Tear down method to clean up after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        del self.storage
        del self.obj

    def test_file_creation(self):
        """Test if file is created upon save."""
        self.storage.new(self.obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_object_storage(self):
        """Test if new object is correctly added to storage."""
        self.storage.new(self.obj)
        self.storage.save()
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, self.storage.all())

    def test_reload_method(self):
        """Test reloading objects from file."""
        self.storage.new(self.obj)
        self.storage.save()
        key = f"BaseModel.{self.obj.id}"
        self.storage.reload()
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
