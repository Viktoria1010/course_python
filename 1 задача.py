a = int(input())


def season(x):
    if x in {1, 2, 12}:
        print('Зима')
    elif x in {3, 4, 5}:
        print('Весна')
    elif x in {6, 7, 8}:
        print('Лето')
    elif x in {9, 10, 11}:
        print('Осень')
    else:
        print('Введите число от 1 до 12')


season(a)