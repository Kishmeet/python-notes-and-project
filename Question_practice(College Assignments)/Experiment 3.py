"""
#1.Check whether given number is divisible by 3 and 5 both
a=int(input("Enter the number to check divisibility: "))
if a%3==0 and a%5==0:
    print("Number is divisible")
else:
    print("Number is not divisiible by 3 and 5")
   
"""
"""
#2.Check whether a given number is multiple of five or not.
n=int(input("Enter an Integer Number "))
if (n%5==0):
    print("Number is a multiple of a 5")
else :
     print("Number is Not a multiple of a 5")

"""
"""
#3.Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.
m=int(input("enter the first number:"))
n=int(input("enter the second number:"))
if m==n:
    print("both of them are equal")
elif m>n:
    print("first is greater")
else:
    print("second is greater")

"""
"""
#4.Find the greatest among three numbers assuming no
#   two values are same.
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))
l=a
if b>l:
    l=b
if c>l:
    l=c
print("The largest number is ",l)

"""
"""
#5.Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
import math
print("Enter Values of coefficent of ax^2+bx+c(i.e.a,b,c)")
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
D=b**2-4*a*c
print(f"Roots of eqauation ({a})x^2+({b})x+{c} are",end=" ")
if(D>0):
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print(f" Real roots and roots are {root1} and {root2} ")
   
elif(D==0):
    root=-b / (2 * a)
    print(f"The equation has one real root: {root}")
    
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-D) / (2 * a)
    print(f"The equation has two imaginary roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
"""
"""
#6.Find whether a given year is a leap year or not
year=int(input("Enter year to check for leap year: "))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("Leap year")
else:
    print("Not a leap year")
"""
"""
#Q7 Write a program which takes any date as input
#   and display next date of the calendar.

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while(1):
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    if day==29 and days_in_month[1] != 29:
            print("Please Enter correct date!")
            break;

    day += 1

    if day > days_in_month[month - 1]:
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    print("Next date is:", year, "-", month, "-", day)
    break;

"""
"""
#Q8 Print the grade sheet of a student for the given range of cgpa.
#   Scan marks of five subjects and calculate the percentage.
pd=int(input("Enter marks in PDS : "))
py=int(input("Enter marks in Python:"))
ch=int(input("Enter marks in Chemistry:"))
en=int(input("Enter marks in English: "))
ph=int(input("Enter marks in Physics :"))
per=(pd+py+ch+en+ph)/5
cgpa=per/10
grade='A'
if cgpa<3.5:
    grade='F'
elif cgpa<5.1:
    grade='C+'
elif cgpa<6.1:
    grade='B'
elif cgpa<7.1:
    grade = 'B+'
elif cgpa<8.1:
    grade = 'A'
elif cgpa<9.1:
    grade = 'A+'
else:
    grade = 'O'
    
print("Gradesheet")
print("Name: Rohit Sharma")
print("Roll number: R17234512            SAP ID: 50005673")
print("Sem 1                               Course: B.Tech CSE AI&ML")
print("\n")
print("Subject Name : Marks")
print("PDS:     ",pd)
print("Phython: ",py)
print("Chemistry: ",ch)
print("English:   ",en)
print("Physics:   ",py)
print("Percentage:",per,"%")
print(f"CGPA:  {cgpa:.1f}")
print("Grade: ",grade)
"""
