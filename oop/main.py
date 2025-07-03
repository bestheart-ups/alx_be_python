# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create library instance
    library = Library()

    # Create book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook1 = EBook("Digital Fortress", "Dan Brown", 5)
    printbook1 = PrintBook("1984", "George Orwell", 328)

    # Add books to library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()