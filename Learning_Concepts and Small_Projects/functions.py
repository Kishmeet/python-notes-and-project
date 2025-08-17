#function A block of reusable code
  # place () after the function name to invoke it
'''def display_invoice(username,amount,due_date):
    print(f"Hello, {username}!")
    print(f"Your amout of ${amount:.2f} is due for {due_date}.")
display_invoice("brocode",100,"01/02/2007")'''
#return Statement use to end a function and sent result back to caller
# default arguments A default value for certain parameters
#                  default is used when that argument
#               is omitted make your functions more flexible, reduces # of arguments
#
# 1.Positional 2.default 3.keyword 4.arbitrary

"""import time
def count(end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("done")
count(10)"""
# keyword arguments an argument preceded by an identifier
#  helps with readability order of arguments doesn't matter
#for x in range(10):
 #   print(x,end=" ")
#print("1","2","3","4","5","6","7","8","9",sep="-")
'''def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)'''
#*args=allow you to pass multiple non-key arguments
#**kwargs=allow you to mass multiple keywords- arguments
#     *unpacking operator
'''def add(*nums):
    return sum(nums)
print(add(1,2,3))
'''
'''
def displa_name(*args):
    print(args)
    for arg in args:
        print(arg, end=" ")
displa_name("kishmeet","sidak","123")

def print_adress(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_adress(state="Uttarakhand",city="dehradun",pincode="248001")

# ----- EXERCISE -----
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")
'''
#lambda functions=A small anonymous function for a one time use (throw away function)
#                 they take any number of arguments,but here only 1 expression
#                 Helps keep that namespace clean and is useful with higher order functions
#                 'sort()','map()','filter()','reduce()'
#                lambda parameter:expression
'''
abc=lambda x:"Even"if x % 2 == 0 else "Odd"
print(abc(10))
double=lambda x:x*2
print(double)
max_value=lambda x,y:x if x > y else y
print(max_value(10,20))
'''
#map(function,collection)=Applies a given function to all the item  in collection
'''
def c_to_f(temp):
    return (temp * 1.8) + 32

celcius_temp=[10,20,30,40,50]
print(map(c_to_f, celcius_temp))
for temp in map(c_to_f, celcius_temp):
   print(temp)
print(list(map(lambda x: "even"if  x%2==0 else "Odd", celcius_temp + [1001])))
'''
#filter(function,collection)=return all the elements that pass a condition
'''
grades=[91,32,83,44,75,56,67]
def is_passing(grade):
    return grade >=60
print(is_passing(91))
print(filter(is_passing,grades))
print(list(filter(is_passing,grades)))
'''
#reduce(function,collection)=Reduces element in a collection to a single value
#                            For Loop is better in most case
#                       Reduce is better for a functional approach + readability
from  functools import reduce
import functools
print(reduce(lambda x,y:x+y, [1,2,3,4,5,6,7,8,9]))
print(dir(functools))
