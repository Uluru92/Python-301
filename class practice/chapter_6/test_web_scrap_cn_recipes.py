import unittest
import math

class TestWebScrapping(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)

if __name__ == "__main__":
    unittest.main()
