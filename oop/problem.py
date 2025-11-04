"""
Designing book system, cloud, e.g. amazon kindle

design application code

Features to be implemented:
1. Users have a library of books that they can add to or remove from
2. Users can set a book from their library as active
3. reading application remembers where a user left off in a given book
4. the reading application only displays a page of text at a time in the active book.

What we need:
class Library:
    library should be mutable, because books inside library will change -> dict
        key: title
        value: book 
    Attributes:
        set only one book to active : int, 1 = active
        or hasing the title
    
    Methods:
        add_book
        remove_book
        

class Book:
    book can be immutable, because content of the book would never change -> tuple
    Attributes:
        title (str)
        pages (tuple(str))
        # page_number (int) => not needed, can use index
        last_page_number (int) (remember off by one error for indexing)
    Methods:
        show_active_page

"""
import logging
import random
from typing import Tuple

logging.basicConfig(level=logging.INFO)


class Book:
    """Book class that cotains title, pages, last_page_number"""

    def __init__(self, title: str, pages: Tuple[str]):
        self.title = title
        self.pages = pages
        self.last_page_number: int = 0
        self.current_page_number: int = 0

    def show_active_page(self):
        """Displays last page of the book"""
        return self.pages[self.last_page_number]

    def turn_page(self, action):
        """Last page number is incremented or decremented when page is turned.

        Given a user's input action, last page number is changed.
        """
        if action == "right":
            self.last_page_number += 1
        elif action == "left":
            if self.last_page_number == 0:
                raise KeyboardInterrupt("Forbidden action")
            self.last_page_number -= 1
        else:
            raise KeyboardInterrupt("Action can either be left or right")

        return self.show_active_page()


class Library:
    """Library class that contains books"""

    def __init__(self):
        self.collection = dict()
        self.active_book = None

    def add_book(self, book: Book):
        """Adding a new book to library

        TODO: add multiple books at once?
        """
        self.collection[book.title] = book.pages

    def remove_book(self, book):
        del self.collection[book.title]

    def open_last_page_of_active_book(self):
        return self.collection[self.active_book].show_active_page()

    def make_book_active(self, book):
        """Make the book selected from user input as active

        TODO: how to avoid hash collision?
        """
        self.active_book = book.title


# pages = ["".join(random.choices("abcdefghijklmopq", k=3)) for _ in range(10)]
pages = ("asdf", "asdfasdf", "qwer", "qwerqwer")

book_one = Book(title="One up Wall Street", pages=pages)
book_two = Book(title="Big Short", pages=pages[::-1])
book_one.turn_page(action=input("Give a user input: "))
dustin_library = Library()

dustin_library.add_book(book_one)
logging.info(f"{dustin_library.select_book(book_one)}")
