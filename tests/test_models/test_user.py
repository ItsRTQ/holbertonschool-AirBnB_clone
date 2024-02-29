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
        self.instance = User()

    def test_email(self):
        self.instance.email = "example@yahoo.com"
        self.assertEqual(self.instance.email, "example@yahoo.com")

    def test_password(self):
        self.instance.password = "password"
        self.assertEqual(self.instance.password, "password")

    def test_firstName(self):
        self.instance.first_name = "name"
        self.assertEqual(self.instance.first_name, "name")

    def test_lastName(self):
        self.instance.last_name = "last Name"
        self.assertEqual(self.instance.last_name, "last Name")
