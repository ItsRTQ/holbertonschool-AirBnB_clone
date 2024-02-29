import unittest
from models.review import Review

class test_cases(unittest.TestCase):

    def test_review_place_id_default_value(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_review_user_id_default_value(self):
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_review_text_default_value(self):
        review = Review()
        self.assertEqual(review.text, "")

    def test_review_attributes_assignment(self):
        place_id = "123"
        user_id = "456"
        text = "Great place to stay!"

        review = Review(
            place_id=place_id,
            user_id=user_id,
            text=text
        )

        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, text)

if __name__ == '__main__':
    unittest.main()