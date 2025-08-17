#Experiment 7: Functions

'"1.Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)"'
'''def find_max_min(numbers):
    if not numbers:
        raise ValueError("The input list is empty.")
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
            
    return max_num, min_num

try:
    user_input = input("Enter a sequence of numbers (space-separated): ")
    numbers = list(map(int, user_input.split()))
    
    max_num, min_num = find_max_min(numbers)
    
    print(f"Maximum number: {max_num}")
    print(f"Minimum number: {min_num}")
    
except ValueError as e:
    print(f"Error: {e}")'''

#2.Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
'''def sum_cube(n):
    sum=0
    for i in range(1,n):
        sum=sum+i**3
    return sum
n=int(input("Enter a Number "))
if n<0:
    print("Invalid Input!")
else:
    print(sum_cube(n))'''
#3.Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
'''def recr(n):
    if n==0:
        return
    else:
        recr(n-1)
        print(n)
n=int(input("Enter value of n:"))
recr(n)'''
#4.Write a recursive function to print Fibonacci series upto n terms.
'''def fib(n):
    if n<=1:
        return n
    else :
        return fib(n-1)+fib(n-2)
n=int(input("Enter number of terms"))
if n<1:
    print("Invalid Input")
else:
    print("Fibonacci Series ")
    for i in range(n):
        print(fib(i))'''
#5. Write a lambda function to find volume of cone.
'''import math
volume=lambda x,y:1/3*math.pi*(x**2)*y
x=int(input("Enter Radius: "))
y=int(input("Enter height: "))
print(volume(x,y))
'''
#6.Write a lambda function which gives tuple of max and min from a list.
#Sample input: [10, 6, 8, 90, 12, 56]
#Sample output: (90,6)
'''find_max_min = lambda lst: (max(lst), min(lst))
user_input = input("Enter a sequence of numbers (space-separated): ")
numbers = list(map(int, user_input.split()))
print(find_max_min(numbers))'''
#7.Write functions to explain mentioned concepts:
#a Keyword argument
'''def greet(name, message):
    print(f"{message}, {name}!")
greet(name="Sir", message="Hello")
#b Default argument
def introduce(name, age=20):
    print(f"My name is {name} and I am {age} years old.")
introduce("kishmeet")  # Uses default age
introduce("kishmeet", 18)  # Overwrites default age
#c Variable length argument
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(10,20,30,40))'''








    
    
