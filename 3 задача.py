x = int(input())
summa = 0

while x > 0:
    ostatok = x % 10
    summa = summa + ostatok
    x = x//10
print('Сумма: ', summa)
