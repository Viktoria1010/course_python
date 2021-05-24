import time

with open('time is 24_05_2021, 19_07.txt', 'w') as to_write:
    start_time = time.time()
    stroka = str(input())
    stroka = stroka.replace(" ", '')
    stroka = stroka.lower()
    stroka_1 = stroka[::-1]
    if stroka == stroka_1:
        print('Палиндром')
    else:
        print('Не палиндром')
    to_write.write(str('%s seconds' % (time.time() - start_time)))
