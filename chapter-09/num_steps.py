from functools import lru_cache

@lru_cache()
def num_steps(num_stairs):
    if num_stairs < 0:
        return 0
    if num_stairs == 0:
        return 1
    if num_stairs == 1:
        return 1

    return num_steps(num_stairs-1) + num_steps(num_stairs-2) + num_steps(num_stairs-3)


import unittest
class NumStepsTests(unittest.TestCase):

    def test_1_step(self):
        self.assertEqual(num_steps(1), 1)

    def test_2_step(self):
        self.assertEqual(num_steps(2), 2)

    def test_3_step(self):
        self.assertEqual(num_steps(3), 4)

if __name__ == '__main__':
    unittest.main()
