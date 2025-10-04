# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
from mymath_DONE import *

class TestRescrape(unittest.TestCase):

    def test_correct_result(self):
        self.assertEqual(subtract_divide(5,4,2),2.5)

    def test_divided_by_zero(self):
        with self.assertRaises(CustomZeroDivsionError):subtract_divide(5,4,4)

if __name__ == "__main__":
    unittest.main()