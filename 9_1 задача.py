import time
import sys


def wait():
    secs = int(input('Введите количество секунд: '))
    while int(secs) >= 0:
        time.sleep(secs)
        secs = int(input('Введите количество секунд: '))
    else:
        sys.exit()


wait()
