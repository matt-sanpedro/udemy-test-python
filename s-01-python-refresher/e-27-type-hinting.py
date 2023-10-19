from typing import List # ,  Tuple, Set, etc...

# type hinting: new feature in Python 3.5+
# "list" data type expected as argument
# "float" data type returned from the function
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

# list_avg(123)

# apply hinting to Book class
# does NOT specify return since class returns nothing
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} g>"

    # return a "Book" of same type currently in
    # created while "Book" class is still processing, cannot just pass Book as variable
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

# list should contain book objects
# will get told if you pass wrong thing by type hint
class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books"
