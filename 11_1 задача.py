class Table:

    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Student(Table):
    def __init__(self, l, w, h, subject):
        super().__init__(l, w, h)
        self.subject = subject
        self.known_subj = [self.subject]

    def study(self, name):
        self.known_subj.append(name)

    def known(self):
        print('These subjects were done: ' + str(self.known_subj))


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Table(1, 3, 0.7)
t_2.outing()

t_3 = Student(2, 5, 8, 'Economics')
t_3.study('Math')
t_3.study('English')
t_3.study('Art')
t_3.known()
