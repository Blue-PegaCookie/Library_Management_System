

# Concept 5 (Advanced): (Advanced End of Python)

# Object-Oriented Programming (OOP) in Python

# I'm about to lay the basics of OOP in Python.

class Car:

    # Construct objects for us
    def __init__(self, make, model, year, color):

        # self refers to the object we're creating
        self.make = make
        self.model = model
        self.year = year
        self.color = color


    # These functions don't need to be in this class as they receive no positional arguments
    def drive(self):
        print("This car is driving.")

    def stop1(self):
        print("This car has stopped.")

    def stop(self):
        print("This car has stopped.")

# We pass only 4 attributes as self is done by itself
car_1 = Car("Toyota", "Corolla", 2021, "Red")
car_2 = Car("Honda", "Civic", 2022, "Blue")
car_3 = Car("Ford", "Mustang", 2023, "Black")
car_4 = Car("Chevrolet", "Camaro", 2024, "White")
car_5 = Car("BMW", "M3", 2025, "Silver")

print(car_5.make)
print(car_5.model)
print(car_5.year)
print(car_5.color)



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

# Pretty impressive, right? Let's move on to the next project.

# I decided to start another project which is way easier!
# I'll come back later to this project and create a programme to access this library management system.


# Programme 1 (EASY)

# Description: Create a system to manage students' information and their grades.

# Class: Student with attributes for student ID, name, and a list of grades.

# Methods: Add a grade, calculate the average grade, and display student information.

# Pillars: Encapsulation (to protect student data), Inheritance (if you want to extend functionality for different types of students).

class student_information:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.__grade = []

    def add_grade(self, grade):
        self.__grade.append(grade)

    def average_grade(self):
        return sum(self.__grade) / len(self.__grade)

    def display_information(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Grades: {self.__grade}")
        print(f"Average Grade: {self.average_grade()}")


student1 = student_information(1, "Alice")
student1.add_grade(80)
student1.add_grade(90)
student1.add_grade(100)

# Programme 2: Inventory Management System (EASY)

# Description: Develop a system to manage inventory for a store.
# Class: Product with attributes for product ID, name, quantity, and price.
# Methods: Add stock, remove stock, and display product information.
# Pillars: Encapsulation (to manage product data), Abstraction (to hide complex stock management logic).

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id
        self.name = name
        self.__quantity = quantity
        self.__price = price

    def add_stock(self, quantity):
        self.__quantity += quantity
        print(f"{quantity} units of {self.name} added to stock.")

    def remove_stock(self, quantity):
        self.__quantity -= quantity
        print(f"{quantity} units of {self.name} removed from stock.")

    def display_info(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.__quantity}")
        print(f"Price: ${self.__price}")

product1 = Product(1, "Laptop", 10, 999.99)
print(product1.name)
product1.add_stock(5)
product1.remove_stock(2)
product1.display_info()


# Project 3: Vehicle Rental System (EASY)

# Description: Build a system to manage vehicle rentals.
# Class: Vehicle with attributes for vehicle ID, type, and availability status.
# Methods: Rent a vehicle, return a vehicle, and display vehicle information.
# Pillars: Inheritance (to create different types of vehicles like Car, Bike), Polymorphism (to handle different rental processes for different vehicle types).

# Base class for Vehicle
class Vehicle:
    def __init__(self, vehicle_id, type):
        self.vehicle_id = vehicle_id
        self.type = type
        self.available = True

    def rent_vehicle(self):
        if self.available:
            self.available = False
            print(f"{self.type} rented successfully.")
        else:
            print(f"{self.type} is not available.")

    def return_vehicle(self):
        if not self.available:
            self.available = True
            print(f"{self.type} returned successfully.")
        else:
            print(f"{self.type} has already been returned.")

    def display_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Type: {self.type}")
        print(f"Available: {self.available}")

# Derived class for Car
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model):
        super().__init__(vehicle_id, "Car")
        self.brand = brand
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

# Derived class for Bike
class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, type):
        super().__init__(vehicle_id, "Bike")
        self.brand = brand
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Type: {self.type}")

# Example usage
car = Car(1, "Toyota", "Corolla")
bike = Bike(2, "Yamaha", "Sport")

car.display_info()
car.rent_vehicle()
car.return_vehicle()

bike.display_info()
bike.rent_vehicle()
bike.return_vehicle()


# Programme 2 (IMPOSSIBLE) E-commerce Platform


# Description: Develop an e-commerce platform that manages products, customers, orders, and payments.

# Requirements:

# Product Class: Attributes for product ID, name, description, price, and stock quantity. Methods to update stock and price.

# Customer Class: Attributes for customer ID, name, email, and a list of orders. Methods to place orders and view order history.

# Order Class: Attributes for order ID, customer ID, list of ordered products, total amount, and order status. Methods to update order status and calculate the total amount.

# Payment Class: Handles payment processing, including payment methods and transaction details.

# EcommercePlatform Class: Manages products, customers, and orders. Methods to add products, register customers, process orders, and handle payments.


# Algorithm Overview:
# Initialize the platform with a collection of products and customers.
# Allow customers to browse products, add them to the cart, and place orders.
# Process payments and update order status.
# Track inventory and update stock quantities after each order.
# Provide functionality to add new products and register new customers.
# Display a list of all products, customers, orders, and payment transactions.


class Product:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def change_stock(self, value):
        self.stock = value
        print(f"{value} units of {self.name} is the new available stock.")

    def change_price(self, value):
        self.price = value
        print(f"{value} is the new price for {self.name}")


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.list_of_orders = []

    def place_order(self, order):
        self.list_of_orders.append(order)
        print(f"Order {order.order_id} placed successfully.")

    def view_order_history(self):
        print(f"Order history for {self.name}:")
        for order in self.list_of_orders:
            print(f"Order ID: {order.order_id}, Total Amount: {order.total_amount}, Status: {order.status}")


class Order:
    def __init__(self, order_id, customer_id, products):
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = products
        self.total_amount = self.calculate_total()
        self.status = 'Pending'

    def update_status(self, status):
        self.status = status
        print(f"Order {self.order_id} status updated to {self.status}.")

    def calculate_total(self):
        return sum(product.price for product in self.products)


class Payment:
    def __init__(self, payment_id, order_id, amount, payment_method):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.payment_method = payment_method
        self.transaction_details = None

    def process_payment(self):
        # Simulate payment processing
        self.transaction_details = f"Payment of {self.amount} using {self.payment_method} processed successfully."
        print(self.transaction_details)


class EcommercePlatform:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added successfully.")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} registered successfully.")

    def process_order(self, order):
        self.orders.append(order)
        customer = next((cust for cust in self.customers if cust.customer_id == order.customer_id), None)
        if customer:
            customer.place_order(order)
            print(f"Order {order.order_id} processed successfully.")
        else:
            print("Customer not found.")

    def handle_payment(self, payment):
        payment.process_payment()
        print(f"Payment {payment.payment_id} handled successfully.")

# Test cases for the EcommercePlatform

# Test case 1: Add a product
product1 = Product(1, "Laptop", "High-end gaming laptop", 1500, 10)
platform = EcommercePlatform()
platform.add_product(product1)

# Test case 2: Register a customer
customer1 = Customer(1, "Alice", "alice@example.com")
platform.register_customer(customer1)

# Test case 3: Place an order
order1 = Order(1, 1, [product1])
platform.process_order(order1)

# Test case 4: View order history
customer1.view_order_history()

# Test case 5: Change product stock
product1.change_stock(20)

# Test case 6: Change product price
product1.change_price(1400)

# Test case 7: Update order status
order1.update_status("Shipped")

# Test case 8: Calculate total amount of an order
print(f"Total amount for order {order1.order_id}: {order1.total_amount}")

# Test case 9: Process a payment
payment1 = Payment(1, 1, order1.total_amount, "Credit Card")
platform.handle_payment(payment1)

# Test case 10: Add another product
product2 = Product(2, "Smartphone", "Latest model smartphone", 800, 50)
platform.add_product(product2)

# Test case 11: Register another customer
customer2 = Customer(2, "Bob", "bob@example.com")
platform.register_customer(customer2)

# Test case 12: Place another order
order2 = Order(2, 2, [product2])
platform.process_order(order2)

# Test case 13: View order history for the second customer
customer2.view_order_history()

# Test case 14: Process another payment
payment2 = Payment(2, 2, order2.total_amount, "PayPal")
platform.handle_payment(payment2)

# Test case 15: Check product stock after orders
print(f"Stock for {product1.name}: {product1.stock}")
print(f"Stock for {product2.name}: {product2.stock}")

# I have successfully created an e-commerce platform using classes in Python.

# I'll be creating a programme to allow users to access this e-commerce platform below.


# 3. Hospital Management System


# Description: Create a hospital management system that manages patients, doctors, appointments, and medical records.

# Requirements:

# Patient Class: Attributes for patient ID, name, age, medical history, and a list of appointments. Methods to add medical records and schedule appointments.
# Doctor Class: Attributes for doctor ID, name, specialty, and a list of appointments. Methods to view and manage appointments.
# Appointment Class: Attributes for appointment ID, patient ID, doctor ID, date, time, and status. Methods to update appointment status and reschedule appointments.
# MedicalRecord Class: Records details of each medical visit, including patient ID, doctor ID, diagnosis, treatment, and prescription.
# Hospital Class: Manages patients, doctors, appointments, and medical records. Methods to add patients, register doctors, schedule appointments, and maintain medical records.


# Algorithm Overview:
# Initialize the hospital with a collection of patients and doctors.
# Allow patients to schedule appointments with doctors based on availability.
# Track and update appointment status.
# Maintain medical records for each patient, including diagnosis and treatment details.
# Provide functionality to add new patients, register new doctors, and manage appointments.
# Display a list of all patients, doctors, appointments, and medical records.


# These projects will help you practice and apply various OOP concepts such as classes, objects, inheritance, encapsulation, and polymorphism.


class Patient:
    def __init__(self, patient_id, name, age, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.appointments = []

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.appointments = []

    def view_appointments(self):
        return self.appointments

    def manage_appointment(self, appointment_id, status):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.status = status

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, status):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status

    def update_status(self, status):
        self.status = status

    def reschedule(self, date, time):
        self.date = date
        self.time = time

class MedicalRecord:
    def __init__(self, patient_id, doctor_id, diagnosis, treatment, prescription):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.prescription = prescription

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.medical_records = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def register_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def add_medical_record(self, record):
        self.medical_records.append(record)

    def display_patients(self):
        for patient in self.patients:
            print(patient.name)

    def display_doctors(self):
        for doctor in self.doctors:
            print(doctor.name)

    def display_appointments(self):
        for appointment in self.appointments:
            print(appointment.appointment_id)

    def display_medical_records(self):
        for record in self.medical_records:
            print(record.diagnosis)

# Test cases for the Hospital Management System

# Test case 1: Add a patient
patient1 = Patient(1, "John Doe", 30, [])
hospital = Hospital()
hospital.add_patient(patient1)

# Test case 2: Register a doctor
doctor1 = Doctor(1, "Dr. Smith", "Cardiology")
hospital.register_doctor(doctor1)

# Test case 3: Schedule an appointment
appointment1 = Appointment(1, 1, 1, "2023-12-01", "10:00", "Scheduled")
hospital.schedule_appointment(appointment1)

# Test case 4: Add a medical record
record1 = MedicalRecord(1, 1, "Flu", "Rest and hydration", "Paracetamol")
hospital.add_medical_record(record1)

# Test case 5: View patient details
hospital.display_patients()

# Test case 6: View doctor details
hospital.display_doctors()

# Test case 7: View appointment details
hospital.display_appointments()

# Test case 8: View medical record details
hospital.display_medical_records()

# Test case 9: Update appointment status
appointment1.update_status("Completed")

# Test case 10: Reschedule an appointment
appointment1.reschedule("2023-12-02", "11:00")

# Test case 11: Add another patient
patient2 = Patient(2, "Jane Doe", 25, [])
hospital.add_patient(patient2)

# Test case 12: Add another doctor
doctor2 = Doctor(2, "Dr. Brown", "Dermatology")
hospital.register_doctor(doctor2)

# Test case 13: Schedule another appointment
appointment2 = Appointment(2, 2, 2, "2023-12-03", "12:00", "Scheduled")
hospital.schedule_appointment(appointment2)

# Test case 14: Add another medical record
record2 = MedicalRecord(2, 2, "Allergy", "Antihistamines", "Cetirizine")
hospital.add_medical_record(record2)

# Test case 15: View all details again
hospital.display_patients()
hospital.display_doctors()
hospital.display_appointments()
hospital.display_medical_records()

# I have successfully created a hospital management system using classes in Python.


