# book_class.py

class Book:
    def _init_(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def _del_(self):
        print(f"Deleting {self.title}")

    def _str_(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def _repr_(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"