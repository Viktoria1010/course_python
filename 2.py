stroka = str(input())
stroka = stroka.replace(' ', '')
stroka = stroka.lower()
a = []
for i in stroka:
    a.append(i)
b = set(a)
if len(a) == len(b):
    print('Нет дублей')
else:
    print('Есть дубли')
print(a, b)