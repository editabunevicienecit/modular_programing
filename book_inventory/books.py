from typing import Any

from helper_functions import *


def get_book_by_title(book_title: str) -> Any | None:
    books = read_file("book_inventory.txt")
    for book in books:
        title = book.split(',')[0].strip()
        if title == book_title:
            return book
    print("Book '{0}' is not in an inventory.".format(book_title))
    return None


def get_book_by_author(book_author: str) -> str:
    books = read_file("book_inventory.txt")
    for book in books:
        author = book.split(',')[1].strip()
        if author == book_author:
            return book
    return "No '{0}' books found in an inventory.".format(book_author)


def get_book_title(book: str) -> str:
    return book.split(',')[0].strip()


def get_book_author(book: str) -> str:
    return book.split(',')[1].strip()


def get_book_copies(book: str) -> str:
    return book.split(',')[2].strip()


def get_book_borrowed_copies(book: str) -> str:
    return book.split(',')[3].strip()


def set_book_title(book: str, title: str):
    book = book.split(',')
    book[0] = title
    book = ','.join(book)
    return book


def set_book_author(book: str, author: str):
    book = book.split(',')
    book[1] = author
    book = ','.join(book)
    return book


def set_book_copies(book: str, copies: str):
    book = book.split(',')
    book[2] = copies
    book = ','.join(book)
    return book


def set_book_borrowed_copies(book: str, borrowed_copies: int):
    book = book.split(',')
    book[3] = str(borrowed_copies)
    book = ','.join(book)
    return book


def update_book(old_book: str, updated_book: str):
    books = read_file("book_inventory.txt")
    updated_books = []
    for book in books:
        if book == old_book:
            updated_books.append(updated_book)
        else:
            updated_books.append(book)

    write_file("book_inventory.txt", updated_books)


def add_book(book: str):
    books = read_file("book_inventory.txt")
    books.append(book)
    write_file("book_inventory.txt", books)


def remove_book(book_remove: str):
    books = read_file("book_inventory.txt")
    updated_books = []
    for book in books:
        if book != book_remove:
            updated_books.append(book)

    write_file("book_inventory.txt", updated_books)


def display_books():
    books = read_file("book_inventory.txt")
    table = []
    headers = "Title, Author, Copies, Borrowed"
    table.append(headers.split(','))
    for book in books:
        table.append(book.split(','))
    for row in table:
        print("{: <50} {: <30} {: <8} {: <8}".format(*row))
