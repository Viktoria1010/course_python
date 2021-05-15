stroka = str(input())
stroka = stroka.replace(" ", '')
stroka = stroka.lower()
stroka_1 = stroka[::-1]
if stroka == stroka_1:
    print('Палиндром')
else:
    print('Не палиндром')