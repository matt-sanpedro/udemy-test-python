# composition is a counterpart to inheritance, it builds other classes using classes
class BookShelf:
    # accepts objects as arguments
    def __init__(self, *books):
        # self.books: a tuple of objects (instantiated from Book class)
        # print(type(books))
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"

"""
Bad approach

Conceptual: 
- a book is NOT a bookshelf
- inheritance, a book is a part of a bookshelf
- not all books are bookshelfs, bookshelf class can be used on its own

Technical:
- book inherits from bookshelf but a __str__ method is defined for book
- thus, the Book class does NOT inherit anything from BookShelf class
"""
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("50 Shades of Grey")
print(book)

book2 = Book("Atomic Habits")
print(book2)

shelf = BookShelf(book, book2)
print(shelf)
