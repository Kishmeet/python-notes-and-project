#1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by
#taking inputs from the user and display details of all students
'''class Student:
    name: str
    sap: str
    marks: list[int, int, int]


students: list[Student] = []

for i in range(3):
    print("-------------------------------")
    name = input(f"Name of student {i + 1}: ")
    sap = input("SAP: ")

    phy = int(input("Marks in Physics: "))
    chem = int(input("Marks in Chemistry: "))
    math = int(input("Marks in Maths: "))

    student = Student()
    student.name = name
    student.sap = sap
    student.marks = [phy, chem, math]

    students.append(student)

print("\n")

for student in students:
    print("Student:", student.name)
    print("SAP:", student.sap)
    print("Marks in Physics:", student.marks[0])
    print("Marks in Chemistry:", student.marks[1])
    print("Marks in Maths:", student.marks[2])

    print("\n")'''

#2.Add constructor in the above class to initialize student details of n students and implement following methods:
'''a)Display() student details
b)Find Marks_percentage() of each student
c)Display result() [Note: if marks in each subject >40% than Pass else Fail]
Write a Function to find average of the class.

import sys

class Student:
    def __init__(self, name: str, sap: str, marks: tuple[int, int, int]) -> None:
        self.name = name
        self.sap = sap
        self.marks = marks

    def Display(self) -> None:
        print("Name:", self.name)
        print("SAP:", self.sap)

        print("Marks in Physics:", self.marks[0])
        print("Marks in Chemistry:", self.marks[1])
        print("Marks in Maths:", self.marks[2])
        print()
        print(f"Percentage: {self.Marks_percentage():.2f}%")

    def Marks_percentage(self) -> float:
        return sum(self.marks) * 100 / (len(self.marks) * 100)

    def result(self) -> str:
        return "Pass" if self.Marks_percentage() > 40.0 else "Fail"


def average(lst_student: list[Student]) -> float:
    return sum(s.Marks_percentage() for s in lst_student) / len(lst_student)


n = int(input("Number of students: "))
if n < 1:
    print("Students cannot be less than 1")
    sys.exit(1)

students: list[Student] = []

for i in range(n):
    print("-------------------------------")
    s_name = input(f"Name of student {i + 1}: ")
    s_sap = input("SAP: ")

    phy = int(input("Marks in Physics: "))
    chem = int(input("Marks in Chemistry: "))
    math = int(input("Marks in Maths: "))

    student = Student(s_name, s_sap, (phy, chem, math))

    students.append(student)

print()
print("============= Details =============")
for student in students:
    student.Display()
    print("Result:", student.result())
    print()
print()
print(f"Average of class: {average(students):.2f}%")
#3. Create programs to implement different types of inheritances.

# Single inheritance
class A:
    pass
class B(A):
    pass
# Multilevel inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass
# Multiple inheritance
class A:
    pass
class B:
    pass
class C(A, B):
    pass
# Heirarchial inheritance
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
# Hybrid inheritance
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
class E(B, C, D):
    pass

#4.Create a class to implement method Overriding.
class Person:
    def display_name(self) -> None:
        raise NotImplementedError()


class Student(Person):
    def __init__(self, name: str) -> None:
        super().__init__()

        self.name = name

    def display_name(self) -> None: # This method has been overridden
        print(self.name)


s = Student(input("Name: "))
s.display_name()
'''

#5. Create a class for operator overloading which adds two Point Objects where Point has x & y values
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, point: "Point") -> "Point":
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

a = Point(10, 20)
b = Point(12, 15)

print(a + b)


