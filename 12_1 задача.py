class Book:
    def __init__(self, name, author, price, rating):
        self.name = name
        self.author = author
        self._price = price
        self.__rating = rating


a = Book("War and Peace", "Leo Tolstoy", 600, 6)
print(a.author)
print(a.name)
print(a._price)
print(a.__rating)
