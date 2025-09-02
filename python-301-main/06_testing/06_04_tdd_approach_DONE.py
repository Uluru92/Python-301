# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

# Pseudocode:
# I am going to test a function called get_life_points()
# The function should increse the attribute called health_points.
# Next, I am going to test a function called get_damaged(), it should decrease the attribute called health_points.

import unittest

def get_life_points(hp):
    hp += 10
    return hp

def get_damage(hp):
    hp -=10
    return hp

class TestInput(unittest.TestCase):
    def test_life_points(self):
        health_points = 76
        self.assertGreater(get_life_points(health_points), health_points)

    def test_get_damage(self):
        health_points = 76
        self.assertLess(get_damage(health_points), health_points)

if __name__ == "__main__":
    unittest.main()
