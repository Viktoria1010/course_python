class Train:

    def __init__(self, cost):
        self.cost = cost
        self.sale = 250
        self._password = ''

    def set_password(self, sign):
        self._password = sign

    def __private(self):
        new_cost = self.cost - self.sale
        print(f'Чшшш, никому не говори, цена в {new_cost} рублей только для тебя.')

    def public(self):
        print(f'Цена билета составляет {self.cost}.')
        if self._password != '':
            parole = input('Введите пароль, если хотете получить скидку: ')
            if parole == self._password:
                self.__private()
            else:
                print(f'Не угадал. Цена билета составляет {self.cost}.')
        else:
            print('Нет пароля. Установите пароль.')


first = Train(783)
first.public()
first.set_password('hallelujah')
first.public()


