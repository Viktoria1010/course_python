import time

current = time.localtime()
date = time.strftime("%Y-%m-%d", current)
current_date = date.split('-')
birth = input('Введите дату рождения (гггг-мм-дд): ')
birthdate = birth.split('-')
how_much_days = 0
if int(birthdate[1]) in range(1, 13):
    if str(birthdate[2]) in {"01", "02", "03", "04", "05", "06", "07", "08", "09"}\
            or int(birthdate[2]) in range(10, 31):
        date = time.strftime("%Y-%m-%d", current)
        years = (int(current_date[0]) - int(birthdate[0]))*365
        month = (int(current_date[1]) - int(birthdate[1]))*30
        days = int(current_date[2]) - int(birthdate[2])
        how_much_days = years + month + days
else:
    print('Несуществующая дата.')
print(how_much_days)  # есть погрешность, конечно, но я, если честно, не знаю, как иначе
