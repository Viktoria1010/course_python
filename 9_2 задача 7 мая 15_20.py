import time

with open('time.txt', 'w') as to_write:
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
