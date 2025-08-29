import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)

class TestMathIsNaN(unittest.TestCase):
    def test_is_not_NaN(self):
        self.assertEqual(math.sqrt(9),3)

if __name__ == "__main__":
    unittest.main()
