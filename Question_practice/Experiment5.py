'''
#Q1 Write a program to count and display the number of capital letters in a given string.

def count_capital_letters(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

string = input("Enter a string: ")
print("Number of capital letters:", count_capital_letters(string))

#Q2 Count total number of vowels in a given string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

#Q3 Input a sentence and print words in separate lines.

sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)

#4.WAP to enter a string and a substring. You have to print the number of times that the
#substring occurs in the given string. String traversal will take place from left to right, not from right to left.
#Sample Input
#ABCDCDC
#CDC
#Sample Output
#2
s=input("Enter a String:")
sub=input("Enter a sub-String:")
cnt = 0
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:  
        cnt += 1
print(cnt)
#5.Given a string containing both upper and lower case alphabets.
#Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
#Sample Input
#ABaBCbGc
#Sample Output
#2A
#3B
#2C
#1G
s=input("Enter a String:").upper()
counts={}
for i in s:
    counts[i] = s.count(i)

for k in counts.keys():
    print(str(counts[k]) + k )
#6.Program to count number of unique words in a given sentence using sets
s=input("Enter a String:")
unique=set(s.split())
print("Unique worda are:")
for k in unique:
    print(str(k))
print("Unique number of words ",len(unique))

#Q7 Create 2 sets s1 and s2 of n fruits each by taking input from user and find:

#a) Fruits which are in both sets s1 and s2
#b) Fruits only in s1 but not in s2
#c) Count of all fruits from s1 and s2

# Taking input for sets s1 and s2
n = int(input("Enter the number of fruits in each set: "))
s1 = set(input("Enter fruit for set s1: ") for i in range(n))
s2 = set(input("Enter fruit for set s2: ") for i in range(n))

# a) Fruits which are in both sets s1 and s2
common_fruits = s1.intersection(s2)
print("Fruits in both sets s1 and s2:", common_fruits)

# b) Fruits only in s1 but not in s2
s1_not_in_s2 = s1.difference(s2)
print("Fruits only in s1 but not in s2:", s1_not_in_s2)

# c) Count of all fruits from s1 and s2
total_fruits = s1.union(s2)
print("Count of all fruits from s1 and s2:", len(total_fruits))
#Q8 Take two sets and apply various set operations on them :

S1 = {Red ,yellow, orange , blue }
S2 = {violet, blue , purple}

# Define the sets
S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

# Set operations
#1 Add
S1.add("green")
print("After adding 'green' to S1:", S1)

#2 Clear
S1_copy = S1.copy()
S1_copy.clear()
print("After clearing S1:", S1_copy)

#3 Copy
S1_copy = S1.copy()
print("Copy of S1:", S1_copy)

#4 Difference
difference = S1.difference(S2)
print("Difference (S1 - S2):", difference)
difference_set_S2_S1 = S2.difference(S1)
print("Difference of S2 - S1:", difference_set_S2_S1)

#5 Difference Update
S1_copy = S1.copy()
S1_copy.difference_update(S2)
print("Difference update (S1 after removing elements found in S2):", S1_copy)

#6 Discard
S1_discard = S1.copy()
S1_discard.discard("blue")
print("After discarding 'blue' from S1:", S1_discard)

#7 Intersection
intersection = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection)

#8 Intersection Update
S1_inter_update = S1.copy()
S1_inter_update.intersection_update(S2)
print("Intersection update (S1 after keeping only elements found in S2):", S1_inter_update)

#9 Is Disjoint
is_disjoint = S1.isdisjoint(S2)
print("Are S1 and S2 disjoint sets?:", is_disjoint)

#10 Is Subset
is_subset = S1.issubset(S2)
print("Is S1 a subset of S2?:", is_subset)

#11 Is Superset
is_superset = S1.issuperset(S2)
print("Is S1 a superset of S2?:", is_superset)

#12 Pop
S1_pop = S1.copy()
popped_element = S1_pop.pop()
print("Popped element from S1:", popped_element)
print("S1 after pop operation:", S1_pop)

#13 Remove
S1_remove = S1.copy()
S1_remove.remove("blue")
print("After removing 'blue' from S1:", S1_remove)

#14 Symmetric Difference
symmetric_difference = S1.symmetric_difference(S2)
print("Symmetric difference between S1 and S2:", symmetric_difference)

#15 Symmetric Difference Update
S1_sym_diff_update = S1.copy()
S1_sym_diff_update.symmetric_difference_update(S2)
print("Symmetric difference update (S1):", S1_sym_diff_update)

#16 Union
union = S1.union(S2)
print("Union of S1 and S2:", union)

#17 Update
S1_update = S1.copy()
S1_update.update(S2)
print("S1 after update with S2:", S1_update)

'''       
