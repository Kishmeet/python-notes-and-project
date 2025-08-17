'''
#Q1 Create two functions (i) That returns a value and (ii) returns no value

# Function that returns a value
def add(a, b):
    return a + b

# Function that returns no value
def sum(a,b):
    print("Sum is ",a+b)

a=int(input("Enter value a:"))
b=int(input("Enter Value b:"))
print("Function add returns sum :",add(a,b))

print("Function sum returns ",sum(a,b))#function returns none



#Q2 Create a python file having functions to compute sum, average, difference, product and division of user
#provided numbers. Demonstrate the accessibility of these functions from some other new python file.
from math_operations import compute_sum, compute_average, compute_difference, compute_product, compute_division
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
print("Sum:", compute_sum(a, b))
print("Average:", compute_average(a, b))
print("Difference:", compute_difference(a, b))
print("Product:", compute_product(a, b))
print("Division:", compute_division(a, b))


#Q3 Highlight using a python code scope of a local and global variables.

x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)



#Q4 Create a nested function and highlight its relevance.  

def outer_function(outer_var):
    def inner_function(inner_var):
        return outer_var + inner_var
    return inner_function

nested = outer_function(10)
print(nested) #Prints the reference to inner_function
print(nested(5))  


#Q5 Can a function be called within another function in Python?

#Yes a function be called within another function in Python:
def greet(name):
    def format_name(n):
        return n.capitalize()
    
    formatted_name = format_name(name)
    return "Hello, " + formatted_name

print(greet("VIRAT"))

#Q6 Can a function return multiple values in Python?

def return_multiple_values():
    a1=int(input("Enter a1: "))
    a2=int(input("Enter a2: "))
    a3=int(input("Enter a3: "))
    return a1,a2,a3

a1,a2,a3 = return_multiple_values()
print("After returning multiple values we got values: ",a1,a2,a3)

#Q7 Can you create a function with default argument values in Python?

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Using the default greeting
print(greet("Alice"))  

# Providing a custom greeting
print(greet("Alice", "Good morning"))

#Q8 Can you write a function that returns another function in Python?
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Getting the inner function
add_five = outer_function(5)#returns inner function 

# Using the returned function
print(add_five(10))  
#Q9 Can you write a function that takes another function
# as an argument and returns a new function in Python?

def outer_function(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Result: {result}"
    
    return inner_function

def add(a, b):
    return a + b

# Passing the add function to outer_function
decorated_add = outer_function(add)

# Using the new function
print(decorated_add(10, 5))  

#10.Write a function that takes a list of numbers
#as an argument and returns the sum of the numbers.
def abc(args):
    a=0
    for arg in args:
        a=a+arg
    return a
numbers=[]
print("ENTER ELEMENTS IN LIST")
while(1):
    n=input("Enter a number or any other character to quit :")
    if n.isdigit():
       n=int(n)
       numbers.append(n)  
    else:
       break
    
print(f"Sum is {abc(numbers)}")

#11.Write a function that takes a list of strings as an argument and
#returns a list of the strings sorted in ascending order.
def sorted_strings(arr):
  n = len(arr)
  for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].upper()> arr[j+1].upper():
                arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
                
        
l=[]
while(1):
    n=input("Enter a String or q/ to quit :")
    if n.lower()=='q/':
        break
    else:
       l.append(n)
print(f"Sorted Strings {sorted_strings(l)}")       

#12.Write a function that takes two lists as arguments and returns a new list that
#contains the elements from both lists,with duplicates removed
def union(list1,list2):
    combined_list = list1 + list2
    unique_elements = []
    for element in combined_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements
l1=[]
l2=[]
print("Enter element for List 1")
while(1):
    n=input("Enter a number or type quit to quit :").strip()
    if n.lower()=='quit':
        break
    else:
       l1.append(n)
print("Enter element for List 2")
       
while(1):
    n=input("Enter a element or type quit to  quit :").strip()
    if n.lower()=='quit':
        break
    else:
       l2.append(n)

print(f"New List {union(l1,l2)}")

#13.Write a function that takes a list of numbers as an argument and returns the largest number in the list.
def largest(args):
    l=0
    for arg in args:
        if arg>l:
          l=arg
    return l    
numbers=[]
while(1):
    n=input("Enter a number or q to quit :")
    if n.lower()=='q':
        break
    else:
       n=int(n)
       numbers.append(n)
print(f"Largest Number in list is {largest(numbers)}")

#14.Write a function that takes a list of numbers and a target number as arguments and
#returns True if the target number is in the list, and False otherwise.
def target(L,t):
    for args in L:
        if t==args:
           return True
    return False
numbers=[]
while(1):
    n=input("Enter a number or any other character to quit :")
    if n.isdigit():
       n=int(n)
       numbers.append(n)  
    else:
       break
t=int(input("Enter a target Number:"))
print(f"{target(numbers,t)}")


#15.Write a function that takes a string as an argument and returns a new string
#that is the reverse of the original string.
def rev(st):
    return st[::-1]
a=input("Enter a String:")
print(f"Reversed String is {rev(a)}")

#16.Write a function that takes a list of numbers as an argument and returns a new list that contains only the even numbers
#from the original list.
def even(num):
    e=[]
    for x in num:
      if x%2==0:
          e.append(x)
    return e
numbers=[]
while(1):
    n=input("Enter a number or any other character to quit :")
    if n.isdigit():
       n=int(n)
       numbers.append(n)  
    else:
       break
print(f"Even Numbers in list are  {even(numbers)}")

#17.Write a function that takes a number n as an argument and returns the sum of the squares of the first n positive integers.
def sumsq(n):
    sum=0
    for x in range(1,n+1):
        sum+=x**2
    return sum      
n=int(input("Enter value of n:"))
print(f"Sum of square of first n positive integers is {sumsq(n)}")
'''
#18.Create a Python function named display_info that takes a person's name as
#the first argument (required) and any number of additional keyword arguments
#representing their personal information (e.g., age, profession, location).
#The function should print out the person's name and all provided information
def display_info(name,**info):
    print(f"Name:{name}")
    for key,value in info.items():
        print(f"{key.capitalize()}:{value}")
name=input("Enter name: ")
info={}
while(1):
    key = input("Enter information type (e.g., age, profession, location) or type 'done' to finish: ").strip().lower()
    if key == 'done':
            break
    value = input(f"Enter {key}: ").strip()
    info[key] = value
display_info(name,**info)  
