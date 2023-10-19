class ClassTest:
    # gets the instance object
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # gets the and used often for factories
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # method does not have self, cls (contains no information of object or class)
    @staticmethod
    def static_method():
        print("Called static_method")

# create new object
test = ClassTest()
test.instance_method()

# class methods does not need instance
ClassTest.class_method()
ClassTest.static_method()

# factory example
class Book:
    # variables become class properties
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book {self.name}, {self.book_type}, weight {self.weight} g"

    # using a classmethod defined inside the class
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

# check class variable TYPES
# print(Book.TYPES)

# create instant of class
book = Book.paperback("50 Shades of Grey", 700)
print(book)

# create instant using the classmethod
book = Book.hardcover("Harry Potter", 1500)
print(book)