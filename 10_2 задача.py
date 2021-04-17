class Subject:

    def __init__(self, name, teacher, length):  # длина измеряется в семестрах
        self.name = name
        self.teacher = teacher
        self.length = length


math = Subject('Math', 'Наталья Ивановна', 2)
eng = Subject('English language', 'Пётр Степанович', 8)
art = Subject('Art', 'Вениамин Рустамович', 1)