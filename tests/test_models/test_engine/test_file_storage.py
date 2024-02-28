import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage 

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Run this method before each test case
        self.file_path = "file.json"
        self.file_storage = FileStorage()
        self.file_storage.reset_filestorage()
        self.obj = BaseModel()
        self.obj.id = "test_id"
        self.obj_name = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.file_storage.new(self.obj)
        self.file_storage.save()

    def tearDown(self):

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path_default_value(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_file_path_invalid(self):
        self.assertIsNot(FileStorage._FileStorage__file_path, "fake.json")

    def test_objects_default_value(self):
        self.file_storage.reset_filestorage()
        self.assertEqual(FileStorage._FileStorage__objects, {})


    def test_all_method(self):
        objects = self.file_storage.all()
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[self.obj_name], self.obj)

    def test_new_method(self):
        new_obj = BaseModel()
        new_obj.id = "new_test_id"
        new_obj_name = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.file_storage.new(new_obj)
        objects = self.file_storage.all()
        expected_objects = {key: obj for key, obj in objects.items() if isinstance(obj, BaseModel)}
        self.assertEqual(objects, expected_objects)

    def test_save_method(self):
        self.file_storage.save()
        with open("file.json", 'r') as file:
            data = json.load(file)
        self.assertIn(self.obj_name, data)
        self.assertEqual(data[self.obj_name], self.obj.to_dict())


    def test_reload_method(self):
        self.file_storage._FileStorage__objects.clear()
        self.file_storage.reload()
        objects = self.file_storage.all()
        expected_objects = {key: obj for key, obj in objects.items() if isinstance(obj, BaseModel)}
        self.assertEqual(objects, expected_objects)
        self.file_storage._FileStorage__objects.clear()
        self.file_storage.reload()
        objects = self.file_storage.all()
        
        # Filter out objects that are not instances of BaseModel
        expected_objects = {key: obj for key, obj in objects.items() if isinstance(obj, BaseModel)}
        
        self.assertEqual(objects, expected_objects)


if __name__ == '__main__':
    unittest.main()
