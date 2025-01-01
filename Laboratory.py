from datetime import datetime, timedelta

def get_non_empty_string_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please enter a valid value.")

def get_date_input(prompt):
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

def get_numeric_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Invalid input. Please enter a positive numeric value.")

def get_isbn_input(prompt):
    while True:
        isbn = input(prompt)
        if len(isbn) == 13 and isbn.isdigit():
            return isbn
        print("Invalid ISBN. Please enter a 13-digit numeric ISBN.")

class Book:
    def __init__(self, title, author, ISBN, borrow_period):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True
        self.borrow_period = borrow_period

    def checkout(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
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
        print("Book is not available.")
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print("Book returned successfully.")
                return True
        print("You have not borrowed this book.")
        return False

class Transaction:
    FINE_RATE = 1  # Default fine rate ($1 per day)

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
                self.fine = overdue_days * self.FINE_RATE
                print(f"Fine for overdue: ${self.fine:.2f}")
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
        if any(m.member_id == member.member_id for m in self.members):
            print("A member with this ID already exists.")
        else:
            self.members.append(member)
            print("Member registered successfully.")

    def find_member(self, member_id):
        return next((member for member in self.members if member.member_id == member_id), None)

    def find_book(self, ISBN):
        return next((book for book in self.books if book.ISBN == ISBN), None)

    def borrow_book(self, member_id, ISBN):
        member = self.find_member(member_id)
        if not member:
            print("Member not found.")
            return

        book = self.find_book(ISBN)
        if not book:
            print("Book not found.")
            return

        if member.borrow_book(book):
            borrow_date = get_date_input("Enter borrow date (YYYY-MM-DD): ")
            transaction = Transaction(member_id, ISBN, book.borrow_period)
            transaction.borrow_book(borrow_date)
            self.transactions.append(transaction)

    def return_book(self, member_id, ISBN):
        member = self.find_member(member_id)
        if not member:
            print("Member not found.")
            return

        book = self.find_book(ISBN)
        if not book:
            print("Book not found.")
            return

        if member.return_book(book):
            return_date = get_date_input("Enter return date (YYYY-MM-DD): ")
            transaction = next((t for t in self.transactions if t.member_id == member_id and t.ISBN == ISBN), None)
            if transaction:
                transaction.return_book(return_date)
            else:
                print("No transaction found for this book and member.")

    def display_books(self):
        print(f"{'Title':<30} {'Author':<20} {'ISBN':<15} {'Availability':<15}")
        print("=" * 80)
        for book in self.books:
            availability = "Available" if book.available else "Checked Out"
            print(f"{book.title:<30} {book.author:<20} {book.ISBN:<15} {availability:<15}")
        print(f"Total books: {len(self.books)}, Borrowed books: {len([b for b in self.books if not b.available])}")

    def display_members(self):
        for member in self.members:
            print(f"Member ID: {member.member_id}, Name: {member.name}")

    def display_transactions(self):
        for t in self.transactions:
            borrow_date = t.borrow_date.strftime('%Y-%m-%d') if t.borrow_date else "N/A"
            return_date = t.return_date.strftime('%Y-%m-%d') if t.return_date else "N/A"
            status = "Overdue" if t.fine > 0 else "On Time"
            print(f"Member ID: {t.member_id}, ISBN: {t.ISBN}, Borrowed: {borrow_date}, Returned: {return_date}, Fine: ${t.fine:.2f}, Status: {status}")

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
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = get_non_empty_string_input("Enter book title: ")
            author = get_non_empty_string_input("Enter book author: ")
            ISBN = get_isbn_input("Enter book ISBN: ")
            borrow_period = get_numeric_input("Enter borrow period (days): ")
            library.add_book(Book(title, author, ISBN, borrow_period))
        elif choice == '2':
            member_id = get_non_empty_string_input("Enter member ID: ")
            name = get_non_empty_string_input("Enter member name: ")
            library.register_member(Member(member_id, name))
        elif choice == '3':
            member_id = get_non_empty_string_input("Enter member ID: ")
            ISBN = get_isbn_input("Enter book ISBN: ")
            library.borrow_book(member_id, ISBN)
        elif choice == '4':
            member_id = get_non_empty_string_input("Enter member ID: ")
            ISBN = get_isbn_input("Enter book ISBN: ")
            library.return_book(member_id, ISBN)
        elif choice == '5':
            library.display_books()
        elif choice == '6':
            library.display_members()
        elif choice == '7':
            library.display_transactions()
        elif choice == '8':
            title = input("Enter book title to search (leave blank to skip): ").strip()
            author = input("Enter book author to search (leave blank to skip): ").strip()
            ISBN = input("Enter book ISBN to search (leave blank to skip): ").strip()
            library.search_books(title=title or None, author=author or None, ISBN=ISBN or None)
        elif choice == '9':
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")

    if __name__ == "__main__":
        Library_Management_System()
