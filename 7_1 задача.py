import unittest


class FirstTask(unittest.TestCase):
    def test_truth(self):
        a = 'dog'
        b = a.lower()
        self.assertTrue(a.islower())
        self.assertFalse(b.isupper())

    def test_in(self):
        rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'violet']
        self.assertIn('magenta', rainbow)
        self.assertNotIn('pink', rainbow)

    def test_greater(self):
        white_russian = {'vodka', 'coffee liquor', 'cream', 'ice'}
        black_russian = {'vodka', 'coffee liquor', 'ice'}
        self.assertGreater(len(white_russian), len(black_russian))

    def test_less(self):
        words = ['cat', 'home', 'cat', 'mom', 'dad', 'I', 'you', 'road', 'mime', 'pig']
        for word in range(len(words)):
            with self.subTest(word=word):
                self.assertLess(len(words[word]), 5)

    def test_equal(self):
        monty_python = {'Terry Jones', 'John Cleese', 'Michel Palin', 'Graham Chapman'}
        comedians = {'Terry Jones', 'John Cleese', 'Michel Palin', 'Graham Chapman'}
        self.assertCountEqual(monty_python, comedians)






if __name__ == '__main__':
    unittest.main()
