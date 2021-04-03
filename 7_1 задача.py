import unittest
import random
import functions_7_1 as fl


class MyTestCase(unittest.TestCase):
    def test_truth(self):
        s = 'SNDGFNRTJ'
        b = fl.truth(s)
        self.assertTrue(b.islower())
        self.assertFalse(s.islower())

    def test_in_rainbow(self):
        rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'violet']
        colors = rainbow
        color_1 = random.choice(colors)
        color_2 = fl.test_in()
        self.assertIn(color_1, rainbow)
        self.assertNotIn(color_2, rainbow)

    def test_greater(self):
        a = int(input())
        b = int(input())
        c = fl.greater(a, b)
        self.assertGreater(c, a)

    def test_less(self):
        length = 4
        word = fl.less()
        self.assertLess(len(word), length)

    def test_equal(self):
        comedians = {'Michel Palin', 'Terry Jones', 'Graham Chapman', 'John Cleese'}
        pythons = fl.equal()
        self.assertEqual(comedians, pythons)


if __name__ == '__main__':
    unittest.main()
