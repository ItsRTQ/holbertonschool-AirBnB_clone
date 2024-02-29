#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from uuid import UUID

class User_test(unittest.TestCase):

    def setUp(self):
        self.instance = User(email="example@yahoo.com", password="password", first_name="name", last_name="last Name")

    def test_user_attributes(self):
        self.assertEqual(self.instance.email, "example@yahoo.com")
        self.assertEqual(self.instance.password, "password")
        self.assertEqual(self.instance.first_name, "name")
        self.assertEqual(self.instance.last_name, "last Name")

if __name__ == '__main__':
    unittest.main()