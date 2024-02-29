import unittest
from models.place import Place

class test_cases(unittest.TestCase):

    def test_place_city_id_default_value(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_place_user_id_default_value(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_place_name_default_value(self):
        place = Place()
        self.assertEqual(place.name, "")

    def test_place_description_default_value(self):
        place = Place()
        self.assertEqual(place.description, "")

    def test_place_number_rooms_default_value(self):
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_place_number_bathrooms_default_value(self):
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_place_max_guest_default_value(self):
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_place_price_by_night_default_value(self):
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_place_latitude_default_value(self):
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_place_longitude_default_value(self):
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_place_amenity_ids_default_value(self):
        place = Place()
        self.assertEqual(place.amenity_ids, [])

    def test_place_attributes_assignment(self):
        city_id = "123"
        user_id = "456"
        name = "Cozy Apartment"
        description = "A beautiful place to stay"
        number_rooms = 2
        number_bathrooms = 1
        max_guest = 4
        price_by_night = 100
        latitude = 37.7749
        longitude = -122.4194
        amenity_ids = ["a1", "a2", "a3"]

        place = Place(
            city_id=city_id,
            user_id=user_id,
            name=name,
            description=description,
            number_rooms=number_rooms,
            number_bathrooms=number_bathrooms,
            max_guest=max_guest,
            price_by_night=price_by_night,
            latitude=latitude,
            longitude=longitude,
            amenity_ids=amenity_ids
        )

        self.assertEqual(place.city_id, city_id)
        self.assertEqual(place.user_id, user_id)
        self.assertEqual(place.name, name)
        self.assertEqual(place.description, description)
        self.assertEqual(place.number_rooms, number_rooms)
        self.assertEqual(place.number_bathrooms, number_bathrooms)
        self.assertEqual(place.max_guest, max_guest)
        self.assertEqual(place.price_by_night, price_by_night)
        self.assertEqual(place.latitude, latitude)
        self.assertEqual(place.longitude, longitude)
        self.assertEqual(place.amenity_ids, amenity_ids)

if __name__ == '__main__':
    unittest.main()