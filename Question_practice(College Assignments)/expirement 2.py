"""
#1.Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a value of 7 to y, perform addition, multiplication, division and subtraction
#on these two variables and Print out the result.
x=9
y=7
z=x+y
print(f"Addition is: {z}")
z=x-y
print(f"Subtraction is: {z}")
z=x*y
print(f"Multiplication is: {z}")
z=x/y
print(f"Division is: {z}")

"""
"""
#2.Write a Program where the radius is taken as input to compute the area of a circle.
r=float(input("Enter the radius of the circle in m's "))
pi=3.14
area=pi*r*r
print(f"Area of circle is {area} m^2")
"""
"""
#3.Write a Python program to solve (x+y)*(x+y)
#Test data : x = 4 , y = 3.Expected output: 49
x=int(input("Enter an integer value "))
y=int(input("Enter an integer value "))
z=(x+y)*(x+y)
print("Output :",z)
"""
"""
#4.Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem. 
a=float(input("Enter the side of the triangle "))
b=float(input("Enter other side of the traiangle "))
c=((a*a)+(b*b))**0.5
print(f"Hypotenuse of the triangle is {c}")

"""
"""
#5.Write a program to find simple interest.
p=float(input("enter the principle amount:"))
r=float(input("enter the rate:"))
t=float(input("enter the time in years:"))
a=p*r*t/100
print("the simple interest is :",a)
"""
"""
#6.Write a program to find area of triangle when length of sides are given.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("The area of the triangle is:",area)
"""
"""
#7. Write a program to convert given seconds into hours, minutes and remaining seconds.
seconds = int(input("Enter the total number of seconds: "))
hours = seconds//3600
sec_left = seconds % 3600
minutes = sec_left // 60
remaining_seconds = sec_left % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)
"""
"""
#8.Write a program to swap two numbers without taking additional variable.
a=int(input("enter the first number :"))
b=int(input("enter the second number:"))
a=a+b
b=a-b
a=a-b
print("after swapping:")
print("first:",a)
print("second:",b)
"""
"""
#Q9 Write a program to find sum of first n natural numbers.
n=int(input("Enter n: "))
a=1
s=(n*(n+1))/2
print("The sum of first ",n,"natural number's is : ",s)
"""
"""
#Q10 Write a program to print truth table for bitwise operators( & , | and ^ operators)
n=int(input("Enter number of bits(2 or 3): "))
if n==2:
    print("Truth table for bitwise operators :")
    print(" A | B | A&B | A|B | A^B ")
    print("---|---|-----|-----|-----")
    for A in [0, 1]:
        for B in [0, 1]:
            print(f" {A} | {B} |  {A&B}  |  {A|B}  |  {A^B} ")
else:
    print(" A | B | C | A&B&C | A|B|C | A^B^C ")
    print("---|---|---|-------|-------|-------")
    for A in [0, 1]:
        for B in [0, 1]:
            for C in [0, 1]:
                print(f" {A} | {B} | {C} |   {A&B&C}   |   {A|B|C}   |   {A^B^C} ")
"""































  
"""
#Q11 Write a program to find left shift and right shift values of a given number.

number = int(input("Enter a number: "))
shifts = int(input("Enter the number of shifts: "))

# Calculate left shift and right shift values
left_shift_value = number << shifts
right_shift_value = number >> shifts

# Output the results
print(f"Left shift value: {left_shift_value}")
print(f"Right shift value: {right_shift_value}")
"""
"""
#Q12 Using membership operator find whether a given number is in sequence (10,20,56,78,89)
a=(10,20,56,78,89)
i=int(input("Enter number to search: "))
if i in a:
    print("Number found")
else:
    print("Number not found")
"""
"""
#Q13 Using membership operator find whether a given character is in a string.
st=input("Enter string: ")
c=input("Enter character to find:")
if c in st:
    print("The character ",c,"is found in the string ",st)
else:
        print("Character not found")

"""





































        







































































































































































































































