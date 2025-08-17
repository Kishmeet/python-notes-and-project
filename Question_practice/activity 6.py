#VARIABLE ARGUMENTS
'''#1)Write a function mean that takes a variable number of integers as input and returns
#their mean (average) as a float
def mean(*numbers: int) -> float:
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0
    
inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("The mean of the numbers is:", mean(*input_data))

#2.Write a function concatenate that takes a variable number of strings as input and returns a single string
#that is the concatenation of all the input strings
def concatenate(*strings: str) -> str:
    output = ""
    for s in strings:
        output += s
    
    return output

inp = input("Enter a sentence: ")
print(concatenate(*inp.split()))
#3. Write a function intersection that takes two or more lists as input
#and returns a list that contains only the elements that are present in
#all the input lists.
def intersection(list_1: list[int], *lists: list[int]) -> list[int]:
    output = []
    for item in list_1:
        if all(item in lst for lst in lists):
            output.append(item)

    return output

n = int(input("How many lists to use: "))
if n <= 1:
    print("Number must be greater than 1")
    exit(-1)
    
lists = []

for _ in range(n):
    inp = input("Enter numbers: ")
    numbers = list(int(x) for x in inp.split())
    lists.append(numbers)

print((intersection(lists[0], *lists[1:])) or "Nothing in common!")
#4)Write a function max_diff that takes a variable number of integers as input
#and returns the maximum difference between any two of the input integers.
def max_diff(*numbers: int) -> int:
    if numbers:
        return abs(max(numbers) - min(numbers))
    else:
        return 0
    
inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("Max difference:", max_diff(*input_data))
#5. Write a function flatten that takes a variable number of lists as input and returns
#a single list that contains all the elements from all the input lists.
def flatten(*lists: list[int]) -> list[int]:
    output = []
    for lst in lists:
        for item in lst:
            output.append(item)

    return output

n = int(input("How many lists to use: "))
if n <= 1:
    print("Number must be greater than 1")
lists = []

for _ in range(n):
    inp = input("Enter numbers: ")
    numbers = list(int(x) for x in inp.split())
    lists.append(numbers)

print("Flattened list: ", flatten(*lists))
#Variable Key-Value Arguments
#1)	Write a function print_info that takes any number of keyword arguments
#as input and prints out each key-value pair on a new line in the format "key: value".
def print_info(**kwargs: str) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")

n = int(input("Enter number of key value pairs: "))
if n < 1:
    print("Number should be 1 or greater!")
    exit(-1)

pairs = {}
print("Enter key value pairs separated by `:` (colon)")

for _ in range(n):
    inp = input("> ")
    if ":" not in inp:
        print("Invalid key value pair!")
        exit(-1)
    
    key, value = inp.split(":", 1)
    pairs[key.strip()] = value.strip()

print_info(**pairs)
#2.Write a function combine_dicts that takes any number of dictionaries as input and
#returns a new dictionary that is the combination of all the input dictionaries.
def combine_dicts(*dicts: dict[str, str]) -> dict[str, str]:
    output = {}
    for d in dicts:
        output.update(d)

    return output

dict1 = { "Name" : "Kishmeet" }
dict2 = { "Age" : "18" }
dict3 = { "University" : "Upes" }

print(combine_dicts(dict1, dict2, dict3))
#3.Write a function count_values that takes any number of arguments as input and returns a dictionary
#where the keys are the input values and the values are the number of times that value appears in the input.
def count_values(*args: int):
    output = {}
    for item in args:
        output[item] = output.get(item, 0) + 1 
    
    print(output)

inp = input("Enter some numbers: ")
numbers = (int(x) for x in inp.split())

count_values(*numbers)
#4.Write a function sort_by_key that takes any number of dictionaries as input and returns a
#list of the input dictionaries sorted by their keys in alphabetical order.
def sort_by_key(*dicts: dict) -> list[dict]:
    output = []

    for d in dicts:
        keys = sorted(list(d.keys()))
        new_dict = {key : d[key] for key in keys}
        output.append(new_dict)

    return output

input_data = ( # The data below has been taken from the internet
    {
        "street": "street()",
        "city": "city()",
        "state": "state()",
        "country": "country()",
        "zip": "zipCode()"
    },
    {
        "message": "Hello, firstName()! Your order number is: #int(1,100)",
        "phoneNumber": "phoneNumber()",
        "phoneVariation": "+90 int(300,399) int(100,999) int(10-99) int(10,99)",
        "status": "enum(active, disabled)"
    },
    {
        "username": "this.name.first-this.name.last",
        "password": "password()",
        "emails": [
        "repeat(2)",
        "email(gmail.com, example.com)"
      ],
    }
)

print(sort_by_key(*input_data))
#5)Write a function calculate_average that takes any number of dictionaries as input, where
#each dictionary has a key "score" with a numerical value, and returns the average of all the scores.
def calculate_average(*dicts: dict[str, int]) -> float:
    if dicts:
        sum = 0

        for d in dicts:
            sum += d.get("score", 0)

        return sum / len(dicts)
    else:
        return 0
    
input_data = (
    {
        "score" : 10
    }, 
    {
        "score" : 20
    },
    {
        "score" : 30
    },
    {
        "score" : 40
    },
    {
        "score" : 50
    },
)

print(calculate_average(*input_data))
#Lambda

#1)Write a lambda function that takes a list of integers as input
#and returns a list of the squares of those integers.
func = lambda x: [num ** 2 for num in x]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))
#2.Write a lambda function that takes a list of strings as input and
#returns a list of the lengths of those strings.
func = lambda x: [len(s) for s in x]
input_data = input("Enter text: ").split()
print(func(input_data))
#3. Write a lambda function that takes a list of tuples as input,
#where each tuple contains two integers, and returns a list of the products of those integers.
func = lambda lot: [first * second for (first, second) in lot]

input_data = [(10, 20), (30, 40), (50, 60)]
print("Input:", input_data)
print("Output:", func(input_data))
#4.Write a lambda function that takes a list of dictionaries as input, where each dictionary contains a "name" key
#and an "age" key, and returns a list of the names of people who are under 18 years old.
func = lambda lst: [item["name"] for item in lst if item["age"] < 18]

input_data = [
    {
        "name" : "Nandu",
        "age" : 19
    },
    {
        "name" : "Viraj",
        "age" : 17
    },
    {
        "name" : "Kishmeet",
        "age" : 18
    },
    {
        "name" : "Rohit",
        "age" : 16
    }
]

print("Under 18:", func(input_data))
#5.Write a lambda function that takes a string as input and returns a new string where every
#other character is capitalized. For example, "hello world" should become "hElLo wOrLd".
func = lambda string: "".join([value.upper() if index % 2 != 0 else value.lower() for index, value in enumerate(string)])

input_data = input("Enter a string: ")
print(func(input_data))
#6.Write a lambda function that takes a list of integers as input and returns a new list with only the even numbers from the input list.
func = lambda lst: [x for x in lst if x % 2 == 0]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))
7)Write a lambda function that takes a list of strings as input and returns a new list with only the strings that start with the letter "a".
func = lambda lst: [x for x in lst if x.startswith("a")]

input_data = input("Enter some text: ").split()
print(func(input_data))
#8)Write a lambda function that takes a list of dictionaries as input, where each dictionary contains a "name" key and an "email" key, and returns a new list with only the dictionaries that have a Gmail email address.
func = lambda lst: [x for x in lst if x["email"].endswith("@gmail.com")]

input_data = [
    {"name": "Ethan Reynolds", "email": "ethan.reynolds@gmail.com"},
    {"name": "Sophia Carter", "email": "sophia.carter@yahoo.com"},
    {"name": "Liam Bennett", "email": "liam.bennett@gmail.com"},
    {"name": "Ava Mitchell", "email": "ava.mitchell@outlook.com"},
    {"name": "Noah Simmons", "email": "noah.simmons@yahoo.com"},
    {"name": "Isabella Hayes", "email": "isabella.hayes@gmail.com"},
    {"name": "Mason Brooks", "email": "mason.brooks@gmail.com"},
    {"name": "Olivia Turner", "email": "olivia.turner@yahoo.com"},
    {"name": "Lucas Murphy", "email": "lucas.murphy@gmail.com"},
    {"name": "Emma Richardson", "email": "emma.richardson@outlook.com"}
]

print(func(input_data))
#9.Write a lambda function that takes a list of integers as input and returns the product of all the numbers in the list.
func = lambda lst: (result := 1, *[result := result * x for x in lst])[-1]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("Product:", func(input_data))
#10.Write a lambda function that takes a string as input and returns a new string with all the vowels removed.
func = lambda string: "".join(x for x in string if x.lower() not in ('a', 'e', 'i', 'o', 'u'))

input_data = input("Enter text: ")
print(func(input_data))
#Lambda with map()

#1)	Write a lambda function that takes a list of integers as input and returns a new list with each integer increased by 1.

func = lambda lst: list(map(lambda x: x+1, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))
#2.Write a lambda function that takes a list of strings as input and returns a new list with each string in all caps.
func = lambda lst: list(map(str.upper, lst))

input_data = input("Enter text: ").split()
print(func(input_data))
#3.Write a lambda function that takes a list of dictionaries as input, where each dictionary contains a "name" key
#and an "age" key, and returns a new list with the ages of each person increased by 1
func = lambda lst: list(map(lambda item: (item, item.update({"age" : item["age"] + 1}))[0], lst))

input_data = [
    {"name": "Ethan Reynolds", "age": 34},
    {"name": "Sophia Carter", "age": 27},
    {"name": "Liam Bennett", "age": 32},
    {"name": "Ava Mitchell", "age": 31},
    {"name": "Noah Simmons", "age": 29},
    {"name": "Isabella Hayes", "age": 54},
    {"name": "Mason Brooks", "age": 44},
    {"name": "Olivia Turner", "age": 41},
    {"name": "Lucas Murphy", "age": 26},
    {"name": "Emma Richardson", "age": 30}
]

print(func(input_data))
#4.Write a lambda function that takes a list of integers as input and returns a new list with only the numbers that are greater than 
func2 = lambda lst: list(map(lambda x: x if x > 5 else None, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func2(input_data))
#5.Write a lambda function that takes a list of strings as input and returns a new list with the length of each string.
func = lambda lst: list(map(len, lst))

input_data = input("Enter text: ").split()
print(func(input_data))
#Lambda with filter()

#1)	Write a lambda function that takes a list of integers as input and returns a new list with only the even numbers from the input list.
func = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))
#2.Write a lambda function that takes a list of strings as input and returns a new list with only the strings that contain the letter "a".
func = lambda lst: list(filter(lambda string: "a" in string.lower(), lst))

input_data = input("Enter text: ").split()
print(func(input_data))
#3) Write a lambda function that takes a list of dictionaries as input, where each dictionary contains a "name" key and an "email" key, and returns a new list with only the dictionaries that have a Gmail email address.
func = lambda lst: list(filter(lambda item: item["email"].endswith("@gmail.com"), lst))

input_data = [
    {"name": "Ethan Reynolds", "email": "ethan.reynolds@gmail.com"},
    {"name": "Sophia Carter", "email": "sophia.carter@yahoo.com"},
    {"name": "Liam Bennett", "email": "liam.bennett@gmail.com"},
    {"name": "Ava Mitchell", "email": "ava.mitchell@outlook.com"},
    {"name": "Noah Simmons", "email": "noah.simmons@yahoo.com"},
    {"name": "Isabella Hayes", "email": "isabella.hayes@gmail.com"},
    {"name": "Mason Brooks", "email": "mason.brooks@gmail.com"},
    {"name": "Olivia Turner", "email": "olivia.turner@yahoo.com"},
    {"name": "Lucas Murphy", "email": "lucas.murphy@gmail.com"},
    {"name": "Emma Richardson", "email": "emma.richardson@outlook.com"}
]

print(func(input_data))
#4)	Write a lambda function that takes a list of integers as input and returns a new list with only the numbers that are greater than 5.
func = lambda lst: list(filter(lambda x: x > 5, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))'''
#5)	Write a lambda function that takes a list of strings as input and returns a new list with only the strings that are at least 5 characters long.

func = lambda lst: list(filter(lambda string: len(string) >= 5, lst))

input_data = input("Enter text: ").split()
print(func(input_data))






































































































