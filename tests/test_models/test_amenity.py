import unittest
from models.amenity import Amenity

class test_cases(unittest.TestCase):

    def test_amenity_name_default_value(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name_assignment(self):
        name = "Swimming Pool"
        amenity = Amenity(name=name)
        self.assertEqual(amenity.name, name)

if __name__ == '__main__':
    unittest.main()