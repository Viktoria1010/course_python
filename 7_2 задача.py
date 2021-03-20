import unittest
import numpy as np


class SecondTask(unittest.TestCase):
    def test_random(self):
        numbers = np.random.randint(1, 100, size=30)
        for number in numbers:
            with self.subTest(number=number):
                self.assertGreaterEqual(number, 0.5)


if __name__ == '__main__':
    unittest.main()
