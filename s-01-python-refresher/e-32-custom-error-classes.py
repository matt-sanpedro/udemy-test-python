# good practice: define errors on top of script
# need to inherit from ValueError or Exception class or will NOT be able to raise it
class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    
    def read(self, pages: int):
        claim_pages = self.pages_read + pages
        if claim_pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {claim_pages} pages, but this book only has {self.page_count} pages"
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")

book = Book("50 Shades of Grey", 100)

# can use try blocks to avoid trace back errors
try:
    book.read(55)
    book.read(70)
except TooManyPagesReadError as e:
    print(f"ERROR: {e}")
