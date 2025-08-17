#1.Write a Python class to represent a circle. The class should have a radius attribute and methods to calculate the area and circumference of the circle
'''import math 
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (self.radius**2)*math.pi
    def circumference(self):
        return 2*(math.pi)*self.radius
c1=Circle(float(input("Enter radius of the circle: ")))
print(c1.area(),c1.circumference())

'''
'''#2.Write a Python class to represent a book. The class should have attributes for the book's title, author, and number of pages.
#It should also have methods to get and set these attributes.
class Book:
    def __init__(self,title,author,number_of_pages):
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
    
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_num_pages(self):
        return self._num_pages

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_num_pages(self, num_pages):
        self._num_pages = num_pages
book1 = Book("", "", 0)
book1.set_title(input("Enter Title: "))
book1.set_author(input("Enter Author: "))
book1.set_num_pages(int(input("Enter Number of pages: ")))
print("Book Details:")
print("Title:", book1.get_title())
print("Author:", book1.get_author())
print("Pages:", book1.get_num_pages())

'''#3.Write a Python class to represent a bank account. The class should have attributes for the account holder's name, account number, and balance.
#It should also have methods to deposit and withdraw money from the account, as well as a method to check the account balance.
'''class BankAccount:
    def __init__(self, holder_name, account_number, balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
    def check_balance(self):
        print(f"{self.holder_name}'s account balance is: ${self.balance:.2f}")
name = input("Enter the account holder's name: ")
acc_number = input("Enter the account number: ")
account = BankAccount(name, acc_number)
while True:
    print("\nWhat would you like to do?")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: $"))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: $"))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please try again.")
#4.Write a Python class to represent a rectangle.
#The class should have attributes for the rectangle's length and width, as well as methods to calculate the area and perimeter of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
rect=Rectangle(10,20)
print(rect.area(),rect.perimeter())

#5.Write a Python class to represent a student. The class should have attributes for the student's name, ID number, and grades.
#It should also have methods to calculate the student's average grade and to print out a summary of their grades.
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def print_summary(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")

name = input("Enter student name: ")
student_id = input("Enter student ID: ")

grades_input = input("Enter grades separated by spaces: ")
grades = [float(g) for g in grades_input.split() if g.replace('.', '', 1).isdigit()]
student = Student(name, student_id, grades)
student.print_summary()

#6.Write a Python class to represent a restaurant. The class should have attributes for the restaurant's name, cuisine type, and number of seats.
#It should also have methods to get and set these attributes, as well as a method to print out a summary of the restaurant's information.
class Restaurant:
    def __init__(self, name, cuisine_type, number_of_seats):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_of_seats = number_of_seats
    def get_name(self):
        return self._name
    def get_cuisine_type(self):
        return self._cuisine_type

    def get_number_of_seats(self):
        return self._number_of_seats
    
    def set_name(self, name):
        self._name = name

    def set_cuisine_type(self, cuisine_type):
        self._cuisine_type = cuisine_type

    def set_number_of_seats(self, seats):
        if seats > 0:
            self._number_of_seats = seats
        else:
            print("Number of seats must be positive.")
    def print_summary(self):
        print("\n--- Restaurant Summary ---")
        print(f"Name: {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Seats: {self.number_of_seats}")
name = input("Enter restaurant name: ")
cuisine = input("Enter cuisine type: ")
seats = int(input("Enter number of seats: "))
restaurant = Restaurant(name, cuisine, seats)
restaurant.print_summary()

#7.Write a Python class Vehicle that has attributes for make, model, and year, and a method get_info that returns
#a string with information about the vehicle.
#Then write a class Car that inherits from Vehicle and has an additional attribute for num_doors and a method get_doors that returns the number of doors.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle Info: {self.year} {self.make} {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_doors(self):
        return f"This car has {self.num_doors} doors."
make = input("Enter the make (e.g., Toyota, Honda): ")
model = input("Enter the model (e.g., Corolla, Civic): ")
year = int(input("Enter the year (e.g., 2020): "))
num_doors = int(input("Enter the number of doors (e.g., 2, 4): "))
my_car = Car(make, model, year, num_doors)
print("The details of your car:")
print(my_car.get_info())
print(my_car.get_doors())
#8.Write a Python class Animal that has attributes for name and species, and a method make_sound that prints out the sound the animal makes.
#Then write a class Dog that inherits from Animal and has an additional attribute
#for breed and a method fetch that prints out the dog fetching a ball.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} the {self.species} says: {sound}")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def fetch(self):
        print(f"{self.name} the {self.breed} runs to fetch the ball!")
name = input("Enter the dog's name: ")
species = "dog"
breed = input("Enter the dog's breed : ")
sound = input("What sound does the dog make?: ")
my_dog = Dog(name, species, breed)
my_dog.make_sound(sound)
my_dog.fetch()

'''
#9.Write a Python class Shape that has attributes for num_sides and area, and a method get_info that returns a string with information about the shap
#Then write a class Triangle that inherits from Shape and has an additional attribute for base and height,
#and a method calculate_area that calculates the area of the triangle.
'''class Shape:
    def __init__(self, num_sides, area=0):
        self.num_sides = num_sides
        self.area = area

    def get_info(self):
        return f"This shape has {self.num_sides} sides and an area of {self.area} square units."


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(num_sides=3)
        self.base = base
        self.height = height

    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle = Triangle(base, height)
triangle.calculate_area()
print(triangle.get_info())

#10Write a Python class Person that has attributes for name, age, and gender, and a method get_info that returns a string with information about the person.
#Then write a class Student that inherits from Person and has an additional attribute for major and a method get_major that returns the student's major
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.gender}."


class Student(Person):
    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major

    def get_major(self):
        return f"{self.name}'s major is {self.major}."
name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
gender = input("Enter the student's gender: ")
major = input("Enter the student's major: ")
student = Student(name, age, gender, major)
print(student.get_info())
print(student.get_major())
'''
#11.Write a Python class BankAccount that has attributes for balance and account_number, and methods deposit and withdraw that add or subtract from
#the balance. Then write a class SavingsAccount that inherits from BankAccount and has an additional attribute for interest_rate and a
#method add_interest that adds interest to the balance based on the interest rate.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")
account_number = input("Enter your account number: ")
balance = float(input("Enter your starting balance: "))
interest_rate = float(input("Enter your interest rate (%): "))
account = SavingsAccount(account_number, balance, interest_rate)
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Add Interest")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.add_interest()
    elif choice == "4":
        print(f"Current balance: ${account.balance:.2f}")
    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice.")




        
#12.Write a Python class Vehicle that has attributes for make, model, and year, and a method get_info that returns a string with information about
#the vehicle. Then write a class Car that inherits from Vehicle and has an additional attribute for num_doors and a
#method get_doors that returns the number of doors.
'''class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} with {self.num_doors} doors"

    def get_doors(self):
        return self.num_doors
make = input("Enter the car's make: ")
model = input("Enter the car's model: ")
year = input("Enter the car's year: ")
num_doors = input("Enter the number of doors: ")
car = Car(make, model, year, num_doors)
print(car.get_info())
'''
#13.Write a Python class Animal that has attributes for name and species, and a method make_sound that prints out the sound the animal makes.
#Then write a class Dog that inherits from Animal and has an additional attribute for breed and a method fetch that prints out the dog fetching a ball.
