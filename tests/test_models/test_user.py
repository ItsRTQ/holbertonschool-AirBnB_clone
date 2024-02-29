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

    def test_email(self):
        self.assertEqual(self.instance.email, "example@yahoo.com")

    def test_password(self):
        self.assertEqual(self.instance.password, "password")

    def test_firstName(self):
        self.assertEqual(self.instance.first_name, "name")

    def test_lastName(self):
        self.assertEqual(self.instance.last_name, "last Name")
