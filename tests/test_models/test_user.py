import unittest
from models.user import User

class TestUserAttributes(unittest.TestCase):

    def test_user_attributes_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_assignment(self):
        email = "test@example.com"
        password = "password123"
        first_name = "John"
        last_name = "Doe"

        user = User(email=email, password=password, first_name=first_name, last_name=last_name)

        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

if __name__ == '__main__':
    unittest.main()
