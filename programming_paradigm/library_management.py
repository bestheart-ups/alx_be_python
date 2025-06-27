# library_management.py

class Book:
    """A class representing a book in the library system."""

    def __init__(self, title, author):
        """
        Initialize a book with title and author.

        Args:
            title (str): Title of the book
            author (str): Author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available (returned)."""
        self._is_checked_out = False

    def is_available(self):
        """
        Check if the book is available for checkout.

        Returns:
            bool: True if available, False if checked out
        """
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Add a book to the library collection.

        Args:
            book (Book): Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")

    def check_out_book(self, title):
        """
        Check out a book by title if it's available.

        Args:
            title (str): Title of the book to check out

        Returns:
            bool: True if successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Return a book by title.

        Args:
            title (str): Title of the book to return

        Returns:
            bool: True if successfully returned, False if book not found or not checked out
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]

        if not available_books:
            print("No books are currently available.")
            return

        for book in available_books:
            print(f"{book.title} by {book.author}")