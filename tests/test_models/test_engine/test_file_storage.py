import unittest
import os
import json
import uuid
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
        objects_after_reload = self.file_storage.all()
        self.assertIn(self.obj_name, objects_after_reload)
        self.assertIsInstance(objects_after_reload[self.obj_name], BaseModel)
        self.assertEqual(objects_after_reload[self.obj_name].id, self.obj.id)

    def test_base_model_save_method(self):
        self.obj.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        self.assertIn(self.obj_name, data)
        serialized_attributes = data[self.obj_name]
        self.assertIn("id", serialized_attributes)
        self.assertIn("created_at", serialized_attributes)
        self.assertIn("updated_at", serialized_attributes)
        self.assertEqual(serialized_attributes["id"], self.obj.id)
        self.assertEqual(serialized_attributes["created_at"], self.obj.created_at.isoformat())
        self.assertEqual(serialized_attributes["updated_at"], self.obj.updated_at.isoformat())

    def test_base_model_save_method(self):
        new_obj = BaseModel()
        new_obj.id = "new_test_id"
        new_obj_name = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_obj.save()
        self.file_storage._FileStorage__objects.clear()
        self.file_storage.reload()
        objects_after_reload = self.file_storage.all()
        self.assertIn(new_obj_name, objects_after_reload)
        self.assertIsInstance(objects_after_reload[new_obj_name], BaseModel)
        self.assertEqual(objects_after_reload[new_obj_name].id, new_obj.id)

if __name__ == '__main__':
    unittest.main()
