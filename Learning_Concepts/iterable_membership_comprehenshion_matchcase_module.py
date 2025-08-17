# Iterables
# An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop
'''
#Membership operators
used to test whether a value or variable is (string, list, tuple, set, or dictionary)
found in a sequence
1. in
2. not in

#List comprehension =
#A concise way to create lists in Python
#       Compact and easier to read than traditional loops
#        [expression for value in iterable if condition]
doubles=[x*2 for x in range(1,11)]
triples=[y*3 for y in range(1,11)]
squares=[z**2 for z in range(1,11)]
print(doubles, triples, squares)
fruits=['apple','banana','mango','orange']
fruit_chars=[fruit[0] for fruit in fruits]
print(fruit_chars)
'''
#Match-case statement (switch): An alternative to using many 'elif' statements
#Execute some code if a value matches a 'case'
#Benefits: cleaner and syntax is more readable
'''def day_of_week(day):
  match day:
    case 1:
      return 'Monday'
    case 2:
      return 'Tuesday'
    case 3:
      return 'Wednesday'
    case 4:
        return 'Thursday'
    case 5:
        return 'Friday'
    case 6:
        return 'Saturday'
    case 7:
        return 'Sunday'
    case _:
        return 'Not a valid date'
print(day_of_week(int(input())))
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Monday"))
'''
#module =a file containing code you want to include in your program
#use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files
#print(help("modules"))
'''
#import math
# import math as m
#from math import e
import module
result = module.pi
print(result)
result = module.square(3)
print(result)
result = module.cube(3)
print(result)
result = module.circumference(3)
print(result)
result = module.area(3)
print(result)'''
##variable scope= where a variable is visible and accessible
#scope resolution= (LEGB) Local > Enclosed -> Global -> Built-in
# ----- LOCAL -----

def func1():
    x = 1 #local
    print(x)

def func2():
    x = 2 #local
    print(x)

func1()
func2()

# ----- ENCLOSED -----

def func1():
    x = 1 #enclosed

    def func2():
        print(x)
    func2()

func1()

# ----- GLOBAL -----

def func1():
    print(x)

def func2():
    print(x)

x = 3 #global

func1()
func2()

# ----- BUILT-IN -----

from math import e

def func1():
    print(e)

func1()