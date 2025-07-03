# library_system.py

class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: '{self.title}' by {self.author}"

class EBook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size  # in MB

    def get_details(self):
        return f"EBook: '{self.title}' by {self.author} - File Size: {self.file_size}MB"

class PrintBook(Book):
    def _init_(self, title, author, page_count):
        super()._init_(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: '{self.title}' by {self.author} - Pages: {self.page_count}"

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book or its subclasses can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book.get_details()}")