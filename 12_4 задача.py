class Date:
    def __init__(self):
        self.__day = 0
        self.__month = 0
        self.__year = 0

    def set_day(self, day):
        if self.__month in {1, 3, 5, 7, 8, 10, 12}:
            if day in range(1, 31):
                self.__day = day
            else:
                print('Неправильное количество дней')
        elif self.__month in {4, 6, 9, 11}:
            if day in range(1, 30):
                self.__day = day
            else:
                print('Неправильное количество дней')
        elif self.__month == 2:
            if day in range(1, 28):
                self.__day = day
            else:
                print('Неправильное количество дней')
        else:
            print('Установите месяц.')

    def set_month(self, month):
        if month in range(1, 12):
            self.__month = month
        else:
            print('Неправильный номер месяца')

    def set_year(self, year):
        self.__year = year

    def get_date(self):
        if self.__year != 0:
            print(f'Current date is {self.__day}-{self.__month}-{self.__year}.')
        else:
            print('Установите год.')


date = Date()
date.set_day(12)
date.set_month(3)
date.set_day(32)
date.set_day(15)
date.get_date()
date.set_year(2892)
date.get_date()





