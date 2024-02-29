import unittest
from models.state import State

class test_cases(unittest.TestCase):

    def test_state_name_default_value(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_assignment(self):
        name = "California"
        state = State(name=name)
        self.assertEqual(state.name, name)

if __name__ == '__main__':
    unittest.main()