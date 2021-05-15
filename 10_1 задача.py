class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author


class Writer:

    def __init__(self, name, books):
        self.name = name
        self.books = books

    def write(self, book):
        if book.author == self.name:
            self.books.append(book.name)

    def print_info(self):
        print(f'Name: {self.name}; books:{self.books}')


book_1 = Book("Romeo and Juliet", "William Shakespeare")
book_2 = Book("It", "Stephen King")
king = Writer("Stephen King", [])

king.print_info()
king.write(book_1)
king.print_info()
king.write(book_2)
king.print_info()
