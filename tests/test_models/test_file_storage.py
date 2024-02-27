import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage for each test case
        self.file_storage = FileStorage()

    def tearDown(self):
        # Remove the file.json created during the tests
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        # Test if all method returns the correct dictionary
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        result = self.file_storage.all()
        expected_result = {
            'BaseModel.{}'.format(obj1.id): obj1.to_dict(),
            'BaseModel.{}'.format(obj2.id): obj2.to_dict()
        }

        self.assertEqual(result, expected_result)

    def test_new_method(self):
        # Test if new method adds the object to the dictionary
        obj = BaseModel()
        self.file_storage.new(obj)

        result = self.file_storage.all()
        expected_result = {'BaseModel.{}'.format(obj.id): obj.to_dict()}

        self.assertEqual(result, expected_result)

    def test_save_and_reload_methods(self):
        # Test if save and reload methods work correctly
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()

        # Create a new instance of FileStorage to reload the data
        new_file_storage = FileStorage()
        new_file_storage.reload()

        result = new_file_storage.all()
        expected_result = {'BaseModel.{}'.format(obj.id): obj.to_dict()}

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
