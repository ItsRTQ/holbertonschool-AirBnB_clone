import unittest
from models.city import City

class test_cases(unittest.TestCase):

    def test_city_state_id_default_value(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_name_default_value(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_city_attributes_assignment(self):
        state_id = "CA"
        name = "San Francisco"
        city = City(state_id=state_id, name=name)
        self.assertEqual(city.state_id, state_id)
        self.assertEqual(city.name, name)

if __name__ == '__main__':
    unittest.main()