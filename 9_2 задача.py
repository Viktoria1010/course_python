import time
import os


disk = 'C:\\'
path = 'Users\\Виктория\\Desktop\\Для Универа\\Второй курс\\Четвертый семестр\\Прога\\course_python\\'
file_name = str("the time is %s.txt" % (format(time.strftime("%Y_%m_%d-%H_%M_%S"))))
whole_path = os.path.join(disk, path, file_name)
start_time = time.time()


def setup():
    with open(whole_path, 'w') as file_to_write:
        file_to_write.write(summa(10101010291938, 5678697083))


def summa(a, b):
    int(a) + int(b)
    t = ' It took %s seconds to solve this' % (time.time() - start_time)
    return t


setup()
