class Worker:
    position = "Worker"

    def __init__(self, name):
        self.name = name
        self.time = 0
        self.salary = 1000

    def give_bigger_salary(self):
        if self.position in {"Manager", "UpperManager"}:
            pass
        else:
            if int(self.time) in {100, 200}:
                self.salary += 250
                print(f'Ok, now your salary is {self.salary}')
            else:
                print("You are not experienced enough, sorry :(")

    def work(self):
        if self.position in {"Manager", "UpperManager"}:
            pass
        else:
            self.time += 20
            print(f"Well, you have worked for {self.time} hours.")

    def give_promotion(self):
        if self.position in {"Manager", "UpperManager"}:
            pass
        else:
            if self.time == 220:
                self.__class__ = Manager
                print(f"You are a {self.position} now. Congrats :)")
            else:
                print('You have to work more.')


class Manager(Worker):
    position = "Manager"

    def __init__(self, name):
        super().__init__(name)
        self.salary = 2500
        self.time = 200

    def give_bigger_salary(self):
        if self.time in {350, 500}:
            self.salary += 500
            print(f'Alright, your salary now is {self.salary}.')

    def work(self):
        self.time += 50
        print(f"Well, you have worked for {self.time} hours.")

    def give_promotion(self):
        if self.time == 500:
            self.__class__ = UpperManager
            print(f"You are a {self.position} now. Congrats :)")
        else:
            print('You have to work more.')


class UpperManager(Worker):
    position = "UpperManager"

    def __init__(self, name):
        super().__init__(name)
        self.salary = 2500
        self.time = 500
        self.max_time = 1000

    def give_bigger_salary(self):
        if self.time in {700, 900}:
            self.salary += 750
            print(f'Well, you were a good worker, so your salary is {self.salary}')
        else:
            print('Work more, dude.')

    def work(self):
        if self.time != self.max_time:
            self.time += 100
            print(f'Wow! You have worked for {self.time} hours!')
        else:
            print('Enough! Go home!')

    def give_promotion(self):
        print("I can't. You are the master already.")


Max = Worker("Max")
Max.work()
Max.work()
Max.give_promotion()
Max.work()
Max.work()
Max.work()
Max.give_bigger_salary()
Max.work()
Max.work()
Max.work()
Max.work()
Max.work()
Max.work()
Max.give_promotion()
Igor = UpperManager("Igor")
