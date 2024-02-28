import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):

        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
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

    def test_objects_default_value(self):
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all_method(self):
        objects = self.file_storage.all()
        self.assertEqual(objects, {self.obj_name: self.obj})

    def test_new_method(self):
        new_obj = BaseModel()
        new_obj.id = "new_test_id"
        new_obj_name = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.file_storage.new(new_obj)
        objects = self.file_storage.all()
        self.assertEqual(objects, {self.obj_name: self.obj, new_obj_name: new_obj})

    def test_save_method(self):
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.assertIn(self.obj_name, data)
            self.assertEqual(data[self.obj_name], self.obj.to_dict())

    def test_reload_method(self):

        new_obj = BaseModel()
        new_obj.id = "new_test_id"
        new_obj_name = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.file_storage.new(new_obj)
        self.file_storage.save()

        self.file_storage._FileStorage__objects = {}

        self.file_storage.reload()

        objects = self.file_storage.all()
        expected_objects = {self.obj_name: self.obj, new_obj_name: new_obj}
        self.assertEqual(objects, expected_objects)

class TestBaseModel(unittest.TestCase):

    def test_save_method(self):
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as file:
            data = json.load(file)
            key_name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key_name, data)
            self.assertEqual(data[key_name], obj.to_dict())

if __name__ == '__main__':
    unittest.main()
