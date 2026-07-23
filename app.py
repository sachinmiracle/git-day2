from datetime import datetime
from typing import List


class Book:
    """Represents a book in a library collection."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def mark_as_borrowed(self) -> None:
        """Marks the book as currently borrowed."""
        self.is_borrowed = True

    def calculate_age(s) -> int:
        """Returns the age of the book in years."""
        current_year = datetime.now().year
        return current_year - s.year

    def __str__(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} ({self.year}) - [{status}]"


class Library:
    """Manages a list of books."""

    def __init__(self):
        self.catalog: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Adds a new book to the library catalog."""
        self.catalog.append(book)
        print(f"Added: {book.title}")

    def list_available_books(self) -> List[Book]:
        """Returns a list of books that are not currently borrowed."""
        return [book for book in self.catalog if not book.is_borrowed]


# --- Usage Example ---
if __name__ == "__main__":
    # Create library instance
    my_library = Library()

    # Add books
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    book2 = Book("1984", "George Orwell", 1949)

    my_library.add_book(book1)
    my_library.add_book(book2)

    # Borrow a book
    book1.mark_as_borrowed()

    print("\n--- Available Books ---")
    for book in my_library.list_available_books():
        print(book)

    print(f"\nYears since '1984' was published: {book2.calculate_age()} years")
