import unittest
import os
import shutil


class ThirdTask(unittest.TestCase):
    def setUp(self) -> None:
        self.path = 'C:\\Users\\Виктория\\Desktop\\Для Универа\\Второй курс\\Четвертый семестр\\Прога\\course_python\\test_third_task'
        os.makedirs(self.path, exist_ok=True)
        with open('C:\\Users\\Виктория\\Desktop\\Для Универа\\Второй курс\\Четвертый семестр\\Прога\\course_python\\test_third_task\\Neo.txt', 'w') as f:
            f.write('Wake up, Neo...The Matrix has you...Follow the white rabbit...Knock, knock, Neo.')

    def test_equality(self):
        with open('C:\\Users\\Виктория\\Desktop\\Для Универа\\Второй курс\\Четвертый семестр\\Прога\\course_python\\test_third_task\\Neo.txt', 'r') as to_check:
            text = to_check.read()
            self.assertTrue(text != '')
            self.assertTrue(text == 'Wake up, Neo...The Matrix has you...Follow the white rabbit...Knock, knock, Neo.')

    def tearDown(self) -> None:
        shutil.rmtree('C:\\Users\\Виктория\\Desktop\\Для Универа\\Второй курс\\Четвертый семестр\\Прога\\course_python\\test_third_task')


if __name__ == '__main__':
    unittest.main()
