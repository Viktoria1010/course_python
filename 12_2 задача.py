class BankAccount:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._balance = 0
        self._password = ''

    def set_balance(self, amount):
        self._balance += amount

    def set_password(self, parole):
        self._password = parole

    def get_balance(self):
        if self._password == '':
            print('Установите пароль.')
        else:
            sign = input('Для получения баланса введите пароль: ')
            if sign == self._password:
                print(f'Баланс Вашего счета {self._balance} P.')
            else:
                print('Пароль неверный. В доступе отказано.')


masha = BankAccount('Masha', 'Petrova')
masha.set_balance(250)
masha.set_balance(43974)
masha.get_balance()
masha.set_password('mammamia')
masha.get_balance()
