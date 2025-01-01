
# Programme 1 (IMPOSSIBLE)
# Library Management System



# Description: Create a library management system that allows users to manage books, members, and borrowing transactions.

# Requirements:

# Book Class: Attributes for title, author, ISBN, and availability status. Methods to check out and return books.
# Member Class: Attributes for member ID, name, and a list of borrowed books. Methods to borrow and return books.
# Library Class: Manages a collection of books and members. Methods to add books, register members, and track borrowing transactions.
# Transaction Class: Records details of each borrowing transaction, including member ID, book ISBN, borrow date, and return date.


from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, ISBN, borrow_period):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True  # By default, the book is available
        self.borrow_period = borrow_period  # The borrow period in days

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
            print("Book was not borrowed.")
            return False

class Member:
    MAX_BORROW_LIMIT = 5

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.borrowed_books:
            print("You have already borrowed this book.")
            return False
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            print("You cannot borrow more than the allowed number of books.")
            return False
        if book.available:
            if book.checkout():
                self.borrowed_books.append(book)
                print("Book borrowed successfully.")
                return True
        else:
            print("Book is not available.")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print("Book has been removed from your borrow list.")
                return True
        else:
            print("You have not borrowed this book.")
            return False

class Transaction:
    def __init__(self, member_id, ISBN, borrow_period):
        self.member_id = member_id
        self.ISBN = ISBN
        self.borrow_date = None
        self.return_date = None
        self.fine = 0
        self.borrow_period = borrow_period

    def borrow_book(self, date):
        self.borrow_date = date

    def return_book(self, date):
        self.return_date = date
        self.calculate_fine()

    def calculate_fine(self):
        if self.return_date and self.borrow_date:
            overdue_days = (self.return_date - self.borrow_date).days - self.borrow_period
            if overdue_days > 0:
                self.fine = overdue_days * 1  # Assuming $1 fine per day
                print(f"Fine for overdue: ${self.fine}")
            else:
                print("No fine. Book returned on time.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        if any(b.ISBN == book.ISBN for b in self.books):
            print("A book with this ISBN already exists.")
        else:
            self.books.append(book)
            print("Book added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully.")

    def get_date_input(self, prompt):
        while True:
            date_str = input(prompt)
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if date > datetime.now().date():
                    print("Date cannot be in the future.")
                else:
                    return date
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def get_numeric_input(self, prompt):
        while True:
            value = input(prompt)
            if value.isdigit():
                return int(value)
            else:
                print("Invalid input. Please enter a numeric value.")

    def get_isbn_input(self, prompt):
        while True:
            isbn = input(prompt)
            if len(isbn) == 13 and isbn.isdigit():
                return isbn
            else:
                print("Invalid ISBN. Please enter a 13-digit numeric ISBN.")

    def borrow_book(self, member_id, ISBN):
        member = self.find_member(member_id)
        book = self.find_book(ISBN)

        if member is None:
            print("Member not found.")
        elif book is None:
            print("Book not found.")
        elif not book.available:
            print("Book is already borrowed by another member.")
        else:
            borrow_date = self.get_date_input("Enter borrow date (YYYY-MM-DD): ")
            if member.borrow_book(book):
                transaction = Transaction(member_id, ISBN, book.borrow_period)
                transaction.borrow_book(borrow_date)
                self.transactions.append(transaction)

    def return_book(self, member_id, ISBN):
        member = self.find_member(member_id)
        book = self.find_book(ISBN)

        if member is None:
            print("Member not found.")
        elif book is None:
            print("Book not found.")
        else:
            if book in member.borrowed_books:
                return_date = self.get_date_input("Enter return date (YYYY-MM-DD): ")
                if member.return_book(book):
                    transaction = next((transaction for transaction in self.transactions if
                                        transaction.member_id == member_id and transaction.ISBN == ISBN), None)
                    if transaction is None:
                        transaction = Transaction(member_id, ISBN, book.borrow_period)
                        self.transactions.append(transaction)
                    transaction.return_book(return_date)
                else:
                    print("This book was not borrowed by you.")

    def display_books(self):
        print(f"{'Title':<30} {'Author':<20} {'ISBN':<15} {'Availability':<15}")
        print("=" * 80)
        for book in self.books:
            availability = "Available" if book.available else "Checked Out"
            print(f"{book.title:<30} {book.author:<20} {book.ISBN:<15} {availability:<15}")
        print(f"Total books: {len(self.books)}, Borrowed books: {len([book for book in self.books if not book.available])}")

    def display_members(self):
        for member in self.members:
            print(f"Member ID: {member.member_id}, Name: {member.name}")

    def display_transactions(self):
        for transaction in self.transactions:
            borrow_date = transaction.borrow_date.strftime('%B %d, %Y') if transaction.borrow_date else "N/A"
            return_date = transaction.return_date.strftime('%B %d, %Y') if transaction.return_date else "N/A"
            overdue_status = "Overdue" if transaction.fine > 0 else "On Time"
            print(f"Member ID: {transaction.member_id}, ISBN: {transaction.ISBN}, Borrowed: {borrow_date}, Returned: {return_date}, Fine: ${transaction.fine}, Status: {overdue_status}")

    def search_books(self, title=None, author=None, ISBN=None):
        results = [book for book in self.books if
                   (title and title.lower() in book.title.lower()) or
                   (author and author.lower() in book.author.lower()) or
                   (ISBN and ISBN == book.ISBN)]
        if results:
            for book in results:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Available: {book.available}")
        else:
            print("No books found.")

    def find_member(self, member_id):
        return next((member for member in self.members if member.member_id == member_id), None)

    def find_book(self, ISBN):
        return next((book for book in self.books if book.ISBN == ISBN), None)

def Library_Management_System():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Display Transactions")
        print("8. Search Books")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            ISBN = library.get_isbn_input("Enter book ISBN: ")
            borrow_period = library.get_numeric_input("Enter borrow period (days): ")
            book = Book(title, author, ISBN, borrow_period)
            library.add_book(book)
        elif choice == '2':
            member_id = library.get_numeric_input("Enter member ID: ")
            name = input("Enter member name: ")
            member = Member(member_id, name)
            library.register_member(member)
        elif choice == '3':
            member_id = library.get_numeric_input("Enter member ID: ")
            ISBN = library.get_isbn_input("Enter book ISBN: ")
            library.borrow_book(member_id, ISBN)
        elif choice == '4':
            member_id = library.get_numeric_input("Enter member ID: ")
            ISBN = library.get_isbn_input("Enter book ISBN: ")
            library.return_book(member_id, ISBN)
        elif choice == '5':
            library.display_books()
        elif choice == '6':
            library.display_members()
        elif choice == '7':
            library.display_transactions()
        elif choice == '8':
            title = input("Enter book title to search (leave blank to skip): ")
            author = input("Enter book author to search (leave blank to skip): ")
            ISBN = input("Enter book ISBN to search (leave blank to skip): ")
            library.search_books(title, author, ISBN)
        elif choice == '9':
            confirm = input("Are you sure you want to exit? (yes/no): ")
            if confirm.lower() == 'yes':
                break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    Library_Management_System()


# I have successfully created a library management system using classes in Python.

# I'll be creating a programme to allow users to access this library management system below.

# End time = 13:02:00
# Total time taken = 15 minutes
