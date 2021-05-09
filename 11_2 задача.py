class Figures:
    name = "Figure"

    def __init__(self, size):
        self.color = 'white'
        self.size = size

    def change_color(self, new_color):
        self.color = new_color

    def change_size(self, new_size):
        self.size = new_size

    def info(self):
        if self.name in {"Oval", 'Square'}:
            pass
        else:
            print(f'The color of mine is {self.color} and the size is {self.size}.')


class Oval(Figures):
    name = 'Oval'

    def __init__(self, size):
        super().__init__(size)

    def info(self):
        print(f"I'm {self.name}, my color is {self.color}, my size is {self.size}.")


class Square(Figures):
    name = 'Square'

    def __init__(self, size):
        super().__init__(size)

    def info(self):
        print(f"My name is {self.name}, I'm {self.color} and I'm {self.size} ft tall.")


triangle = Figures(18)
triangle.info()
triangle.change_color('blue')
triangle.info()
oval = Oval(15)
oval.info()
oval.change_color('violet')
oval.change_size(19)
oval.info()
square = Square(764)
square.info()
