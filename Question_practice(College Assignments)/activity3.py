#1.Initialize the below mentioned data types do the following:
#a.Create numeric, string, tuple, list and dictionary data type.
a=10
b=10.5
s="abcde"
L= ["apple", "banana", "cherry","coconut"]
T=("apple","banana","cherry","coconut")
D={'name':'Bob','age':40}
#b.Use type function to identify the class.
print(type(a))
print(type(b))
print(type(s))
print(type(L))
print(type(T))
print(type(D))
#c.Display the list of methods supported by the data type using Dir function
print(dir(a))
print(dir(b))
print(dir(s))
print(dir(L))
print(dir(T))
print(dir(D))
#d.Implement any five listed methods for each data type
#numeric
print(abs(a))
print(max(a,b))
print(pow(a,2))
print(min(a,b))
print(round(b))
#String
print(len(s))
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.isalpha())
#Lists
print(dir(L))
print(help(L))
print(len(L))
print(L.index("cherry"))
print(L.count("cherry"))
#tuple
print(dir(T))
print(help(T))
print(len(T))
print(T.index("cherry"))
print(T.count("cherry"))
#dictonary
print(D. keys())
print(D.values())
print(D.items())
b=D. copy()
print(b)
D.clear()
print(D)
#..............................................................................................................................................................................................
#2.Using a suitable example test the mutability of aforementioned data types.
#Strings are Immutable, Strings cannot be modified; instead, create a new one.
s="GATTCHA"
# s[3]=c //TypeError: object doesn't support item assignment
s = s.replace("G","U")
print(s)
#List are muttable
L=["apple", "banana", "cherry","coconut"]
L[3]="kiwi"
print(L)
#Tuples are Immutable.
fruits=("apple","banana","cherry","coconut")
# fruits[1]="aa" //TypeError: 'tuple' object does not support item assignment

#Dictonary are mutable.
super_hero_names = {'Superman' : 'Clark Kent','Spiderman' : 'Peter Parker'}

super_hero_names['Batman'] = 'Bruce Wayne' 

print(super_hero_names)
#........................................................................................................................................................................................
#3.Initialize a sentence “This is too easy to handle” and capitalize each word.
s="This is too easy to handle"
print(s.title())
#........................................................................................................................................................................................
#4.Write a program that takes a string as input and removes all whitespace characters (spaces, tabs) from it.
string = input("enter a string ")
string=string.replace(" ", "")
print(string)
#.......................................................................................................................................................................................
#5.Write a program that takes a string and a substring as input and prints the index of the first occurrence of the substring in the string
string = input("enter a string")
s = input("enter a substring")
print(string.find(s))
#........................................................................................................................................................................................
#6.Insert in a list an item at the start, middle and end of a list.
a=[1,2,4,7]
a.append(6)
a.insert(0,6)
b=len(a)//2
a.insert(b,6)
print(a)
#..........................................................................................................................................................................................
#7.Write a program that takes a list of numbers as input and prints the sum of all elements.
a=[]
n=int(input("Enter the no of items in the list:"))
for i in range(n):
    k=int(input("enter the value to be added:"))
    a.append(k)
print(a)
l=sum(a)
print("the sum of the list is :",l)
#..........................................................................................................................................................................................
#8.Write a program that takes a list and an element as input, and prints the index of the first occurrence of the element in the list
L=[]
while True:
    l= input("enter list items or q to quit: ")
    if (l.lower() == "q"):
        break
    else :
     L.append(l)

s=input("enter element to search for: ")
print(L.index(s))
#.........................................................................................................................................................................................
#9.Print all values of a dictionary.
d = {'name':'bob','age':40,'eggs':3}
print(d.values())
#..........................................................................................................................................................................................
#10. Create a nested list and print any three items using index values.
groceries=[["apple","banana","cherry","kiwi"],
           ["carrot","potato","tomato"],
           ["pork","beef","chicken"]]
print(groceries)
print(groceries[0])
print(groceries[0][2])
print(groceries[2][1])


s="This is too easy to handle"
print(s.title())
#.......................................................................................................................................................................................
#11.Remove a value from a dictionary using the key value and insert a new key value pair in the same dictionary.
dict1 = {1: "one", 2: "two", 3: "three", 4: "four"}
print("Original Dictionary: ", dict1)
valDel = dict1.pop(1)
print("Dictionary after using pop(): ", dict1)
print("The value that was removed is: ", valDel)
dict1[10]='ten'
print("New Dictionary ",dict1)
#.......................................................................................................................................................................................
#12.Write a program that takes a dictionary as input and prints the dictionary sorted by keys.
d={}
while True:
    a = input("Enter key")
    b = input("Enter Value")
    d[a]=b
    ab = input("do you want to continue(y/n)")
    if ab == 'n' or ab == 'N':
        break;
d = dict(sorted(d.items()))
print(d)
#.......................................................................................................................................................................................
#13.Write a program that takes a dictionary and a key-value pair as input and updates the dictionary with the new value for the given key.
d2={}
while True:
    a = input("Enter key")
    b = input("Enter Value")
    d2[a]=b
    ab = input("do you want to continue(y/n)")
    if ab == 'n' or ab == 'N':
        break;
print("Dictionary is: ",d2)
a11 = input("Enter key: ")
a12 = input("Enter Value: ")
d2.update({a11:a12})
print(d2)
#.......................................................................................................................................................................................
#14.	Write a program that takes two dictionaries as input and prints the common keys between them.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_keys = set(dict1.keys()).intersection(set(dict2.keys()))
print("Common keys between the two dictionaries:", common_keys)
#.......................................................................................................................................................................................
#15.	Validate the statement “Tuples have duplicate items”.
#In Python, tuples are ordered collections of items, and they can contain duplicate items.
#To demonstrate this, let's create a tuple with duplicate items and see how Python handles it.
# Creating a tuple with duplicate items
t = (1, 2, 2, 3, 4, 4, 4, 5)

# Printing the tuple
print("Tuple with duplicate items:",t)
#.......................................................................................................................................................................................





















































































































