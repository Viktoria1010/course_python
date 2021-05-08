class Train:
    _password = 'icecream'

    def __init__(self, cost):
        self.cost = cost
        self.sale = 250

    def __private(self):
        new_cost = self.cost - self.sale
        print(f'Чшшш, никому не говори, цена в {new_cost} рублей только для тебя.')

    def public(self):
        print(f'Цена билета составляет {self.cost}.')
        parole = input('Введите пароль, если хотете получить скидку: ')
        if parole == self._password:
            self.__private()
        else:
            print(f'Не угадал. Цена билета составляет {self.cost}.')


first = Train(783)
first.public()
first.__private()
