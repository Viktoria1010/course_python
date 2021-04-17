class Circle:
    name = 'Circle'

    def __init__(self, color, size, box):
        self.color = color
        self.size = size
        self.box = box


class Triangle:
    name = 'Triangle'

    def __init__(self, color, size, box):
        self.color = color
        self.size = size
        self.box = box


class Rectangle:
    name = 'Rectangle'

    def __init__(self, color, size, box):
        self.color = color
        self.size = size
        self.box = box


class Star:
    name = 'Star'

    def __init__(self, color, size, points, box):
        self.color = color
        self.size = size
        self.points = points
        self.box = box


class Box:

    def __init__(self, name, figures):
        self.name = name
        self.figures = figures

    def put_in(self, figure):
        if figure.box == '':
            self.figures.append([figure.name, figure.color, figure.size])
            figure.box = self.name
        else:
            print(figure.name + ' is already in the box.')

    def print_info(self):
        print(f'Figures: {self.figures}')


circle = Circle('pink', 2, '')
triangle = Triangle('magenta', 8, '')
rectangle = Rectangle('orange', 0.4, '')
star = Star('violet', 19, 9, '')
box_1 = Box('Box 1', [])
box_2 = Box('Box 2', [])
box_1.put_in(circle)
box_1.put_in(star)
box_1.print_info()
box_2.put_in(star)
box_2.put_in(rectangle)
box_2.print_info()
