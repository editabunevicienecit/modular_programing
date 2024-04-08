from books import *
from borrowings import *
from helper_functions import *


def borrow_book():
    name = get_non_empty_string("Name >>> ", 1, 20)
    membership = get_positive_number("Membership number >>> ", 100000, 999999)
    times_borrowed = len(get_borrowing_by_membership(str(membership)))
    if times_borrowed < 4:
        book_title = get_non_empty_string("Book title >>> ", 0, 50)
        book = get_book_by_title(book_title)
        if book:
            print(book)
            book_copies = get_book_copies(book)
            book_borrowings = get_book_borrowed_copies(book)
            copies_available = int(book_copies) - int(book_borrowings)
            if copies_available != 0:
                print("Yoy can borrow this book.")
                new_borrowing = "{0}, {1}, {2}, {3}".format(name, membership, book_title, str(date.today()))
                add_borrowing(new_borrowing)
                new_book = book
                new_book = set_book_borrowed_copies(new_book, int(get_book_borrowed_copies(new_book)) + 1)
                update_book(book, new_book)
            else:
                print("No available copies left of this book.")

    else:
        print("You borrowed too many books, please return some.")


def return_book():
    name = get_non_empty_string("Name >>> ", 1, 20)
    membership = get_positive_number("Membership number >>> ", 100000, 999999)
    member_borrowings = get_borrowing_by_membership(str(membership))
    display_borrowings(member_borrowings)
    print("")
    book_to_return_title = get_non_empty_string("Title of the book you wish to return >>> ", 0, 50)
    borrowing_record = ([b for b in member_borrowings if book_to_return_title in b])[0]
    if borrowing_record:
        borrowed_date = get_borrowing_date(borrowing_record)
        today_date = date.today()
        overdue = (today_date - borrowed_date).days
        if overdue > 7:
            days_overdue = overdue - 7
            penalty = days_overdue * 2
            print("You are overdue {0} days. Please pay {1} Eur.".format(days_overdue, penalty))
        remove_borrowing(borrowing_record)
        book = get_book_by_title(book_to_return_title)
        new_book = book
        new_book = set_book_borrowed_copies(new_book, int(get_book_borrowed_copies(new_book)) - 1)
        update_book(book, new_book)
    else:
        print("Book is not in the list")

def show_admin_menu():
    display_books()
    print("")
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Update available copies")
    print("4. Main Menu")
    print("")


def show_main_menu():
    print("")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Review Borrowed Books")
    print("4. Manage Inventory")
    print("5. Exit")
    print("")


def main():
    while True:
        show_main_menu()
        option = get_positive_number("Please select an option >>> ", 1, 5)
        if option == 1:
            borrow_book()
        elif option == 2:
            return_book()
        elif option == 3:
            print ("not implemented")
        elif option == 4:
            print("not implemented")
        elif option == 5:
            break


main()