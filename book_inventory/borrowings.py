from datetime import datetime, date, timedelta
from typing import List, Any

from helper_functions import *


def get_borrowing_by_borrowers_name(borrowers_name: str) -> str:
    borrowings = read_file("borrowed_books.txt")
    for borrowing in borrowings:
        borrower = borrowing.split(',')[0].strip()
        if borrower == borrowers_name:
            return borrowing
    return "'{0}' has no book borrowings.".format(borrowers_name)


def get_borrowing_by_membership(membership_number: str) -> list[Any]:
    borrowings = read_file("borrowed_books.txt")
    member_borrowings = []
    for borrowing in borrowings:
        membership = borrowing.split(',')[1].strip()
        if membership == membership_number:
            member_borrowings.append(borrowing)
    return member_borrowings


def get_borrowing_name(borrowing: str) -> str:
    return borrowing.split(',')[0].strip()


def get_borrowing_membership(borrowing: str) -> str:
    return borrowing.split(',')[1].strip()


def get_borrowing_book(borrowing: str) -> str:
    return borrowing.split(',')[2].strip()


def get_borrowing_date(borrowing: str) -> date:
    borrowing_date = borrowing.split(',')[3].strip()
    return datetime.fromisoformat(borrowing_date).date()


def set_borrowing_name(borrowing: str, name: str):
    borrowing = borrowing.split(',')
    borrowing[0] = name
    borrowing = ','.join(borrowing)
    return borrowing


def set_borrowing_membership(borrowing: str, membership: str):
    borrowing = borrowing.split(',')
    borrowing[1] = membership
    borrowing = ','.join(borrowing)
    return borrowing


def set_borrowing_book(borrowing: str, book: str):
    borrowing = borrowing.split(',')
    borrowing[2] = book
    borrowing = ','.join(borrowing)
    return borrowing


def set_borrowing_date(borrowing: str, date: str):
    borrowing = borrowing.split(',')
    borrowing[2] = date
    borrowing = ','.join(borrowing)
    return borrowing


def update_borrowing(old_borrowing: str, updated_borrowing: str):
    borrowings = read_file("borrowed_books.txt")
    updated_borrowings = []
    for borrowing in borrowings:
        if borrowing == old_borrowing:
            updated_borrowings.append(updated_borrowing)
        else:
            updated_borrowings.append(borrowing)

    write_file("borrowed_books.txt", updated_borrowings)


def add_borrowing(borrowing: str):
    borrowings = read_file("borrowed_books.txt")
    borrowings.append(borrowing)
    write_file("borrowed_books.txt", borrowings)


def remove_borrowing(borrowing_remove: str):
    borrowings = read_file("borrowed_books.txt")
    updated_borrowings = []
    for borrowing in borrowings:
        if borrowing != borrowing_remove:
            updated_borrowings.append(borrowing)

    write_file("borrowed_books.txt", updated_borrowings)


def display_borrowings(borrowings: list):
    table = []
    headers = "Name, Membership, Book title, Borrow date"
    table.append(headers.split(','))
    for borrowing in borrowings:
        table.append(borrowing.split(','))
    for row in table:
        print("{: <15} {: <15} {: <50} {: <15}".format(*row))


def display_all_borrowings_with_due_date(borrowings=None):
    if borrowings is None:
        borrowings = read_file("borrowed_books.txt")
    table = []
    headers = "Name, Membership, Book title, Borrow date, Due Date"
    table.append(headers.split(','))
    for borrowing in borrowings:
        borrowing_array = borrowing.split(',')
        borrow_date = datetime.fromisoformat(borrowing_array[3].strip()).date()
        due_date = borrow_date + timedelta(days=7)
        borrowing_array.append(str(due_date))
        table.append(borrowing_array)

    for row in table:
        print("{: <15} {: <15} {: <50} {: <20} {: <20}".format(*row))


def display_all_borrowings():
    borrowings = read_file("borrowed_books.txt")
    table = []
    headers = "Name, Membership, Book title, Borrow date"
    table.append(headers.split(','))
    for borrowing in borrowings:
        table.append(borrowing.split(','))
    for row in table:
        print("{: <50} {: <15} {: <50} {: <15}".format(*row))
