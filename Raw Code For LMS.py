
# Programme 1 (IMPOSSIBLE)
# Library Management System



# Description: Create a library management system that allows users to manage books, members, and borrowing transactions.

# Requirements:

# Book Class: Attributes for title, author, ISBN, and availability status. Methods to check out and return books.
# Member Class: Attributes for member ID, name, and a list of borrowed books. Methods to borrow and return books.
# Library Class: Manages a collection of books and members. Methods to add books, register members, and track borrowing transactions.
# Transaction Class: Records details of each borrowing transaction, including member ID, book ISBN, borrow date, and return date.

# start_time = 12:47:00

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print("Book checked out successfully.")
            return True
        else:
            print("Book is not available.")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book has been placed back in the library.")
            return True
        else:
            print("Book has not been borrowed.")
            return False

#Testing out the Book class

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
# print(book1.checkout())
# print(book1.return_book())

# Test Successful (For basic understanding, I have not done data types tests)

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.checkout():
            self.borrowed_books.append(book)
            print("Book borrowed successfully.")
        else:
            print("Book is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print("Book has been removed from your borrow list.")
        else:
            print("You have not borrowed this book.")

#Testing out the Member class

# member1 = Member(1, "Alice")
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
# member1.borrow_book(book2)
# member1.return_book(book2)

# Test Successful (For basic understanding, I have not done data types tests)

class Transaction:
    def __init__(self, member_id, ISBN):
        self.member_id = member_id
        self.ISBN = ISBN
        self.borrow_date = None
        self.return_date = None

    def borrow_book(self, date):
        self.borrow_date = date

    def return_book(self, date):
        self.return_date = date


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully.")

    def borrow_book(self, member_id, ISBN):
        member = next((member for member in self.members if member.member_id == member_id), None)
        book = next((book for book in self.books if book.ISBN == ISBN), None)

        if member is None:
            print("Member not found.")
        elif book is None:
            print("Book not found.")
        else:
            member.borrow_book(book)
            transaction = Transaction(member_id, ISBN)
            transaction.borrow_book("2021-12-31")  # Example date
            self.transactions.append(transaction)

    def return_book(self, member_id, ISBN):
        member = next((member for member in self.members if member.member_id == member_id), None)
        book = next((book for book in self.books if book.ISBN == ISBN), None)

        if member is None:
            print("Member not found.")
        elif book is None:
            print("Book not found.")
        else:
            member.return_book(book)
            transaction = next((transaction for transaction in self.transactions if transaction.member_id == member_id and transaction.ISBN == ISBN), None)
            if transaction is not None:
                transaction.return_book("2021-12-31")  # Example date
            else:
                print("Transaction not found.")

# Create a library instance
# library = Library()

# Add books to the library
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
# library.add_book(book1)
# library.add_book(book2)

# Register a member
# member1 = Member(1, "Alice")
# library.register_member(member1)

# Borrow and return a book
# library.borrow_book(1, "9780061120084")
# library.return_book(1, "9780061120084")

# I have successfully created a library management system using classes in Python.

# I'll be creating a programme to allow users to access this library management system below.

# End time = 13:02:00
# Total time taken = 15 minutes
