#1.Write a Python program that takes two integers as input from the user and divides them. Handle the ZeroDivisionError
#exception and print an appropriate message if the user enters 0 as the second input.
'''try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = num1 / num2
    print(f"The result of division is: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero second number.")
except ValueError:
    print("Error: Please enter valid integers.")'''
#2.Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list.
#Handle the TypeError exception and return None if the input list is not valid.
'''def sum_even_numbers(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input is not a valid list.")
        total = 0
        for num in numbers:
            if isinstance(num, int) or isinstance(num, float):
                if num % 2 == 0:
                    total += num
            else:
                raise TypeError("List contains non-numeric elements.")
        
        return total
    
    except TypeError as e:
        print(f"Error: {e}")
        return None
input = input("Enter a list of numbers separated by spaces: ")
try:
    numbers = [float(x) for x in input.split()]
    result = sum_even_numbers(numbers)
    if result is not None:
        print(f"Sum of even numbers: {result}")
    else:
        print("Invalid input.")
    
except ValueError:
    print("Error: Please enter valid numbers.")'''
#3.Write a Python program that reads a text file and counts the number of words in it.
#Handle the FileNotFoundError exception and print an appropriate message if the file is not found.
'''def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()  
            words = content.split()  
            return len(words)  

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
filename = input("Enter the filename: ")
word_count = count_words_in_file(filename)
if word_count is not None:
    print(f"The number of words in the file '{filename}' is: {word_count}")'''
#4.Write a Python function that takes a string as input and returns the number of vowels in it.
#Handle the ValueError exception and return None if the input string is not valid.
'''def count_vowels(input_string):
    try:
        vowels = "aeiouAEIOU"
        count = 0
        for char in input_string:
            if char in vowels:
                count += 1
        
        return count
    except ValueError:
        return None
print("Number of vowels are :",count_vowels(input("Enter a string ")))'''
#5.Write a Python program that prompts the user to enter their age and calculates the year they will turn 100.
#Handle the ValueError exception and print an appropriate message if the user enters an invalid age.
'''def calculate_year_turn_100():
    try:
        age = int(input("Please enter your age: "))
        if age>0:
         current_year = 2025
         year_turn_100 = current_year + (100 - age)
         print(f"You will turn 100 years old in the year {year_turn_100}.")
        else:
             print("Invalid input! Please enter a valid integer for your age.")
    except ValueError:
        print("Invalid input! Please enter a valid integer for your age.")
calculate_year_turn_100()'''
#6. Write a Python function divide() that takes two integers as input and divides them. The function should print the result of the division and also print a message indicating whether the division was successful or not. If the division was successful, the message should say "Division successful." If the division was not successful (i.e., if the user tries to divide by 0), the message should say "Division failed." In either case, the function should close any open resources before returning.
'''Sample Output
>>> divide(6, 2)
3.0
Division successful.

>>> divide(6, 0)
Division failed.
def divide(a,b):
   try:
       div=a/b
       print(div)
       print("Division successful.")
   except ZeroDivisionError:
       print("Division failed.")
a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))
divide(a,b)'''
#7. Write a Python function that takes a list of strings as input and returns the first string that has a length greater than 10. Handle the IndexError exception and return None if the input list is empty.
'''def find_long_string(strings):
    try:
        for string in strings:
            if len(string) > 10:
                return string
        return None
    except IndexError:
        return None
a = input("Enter a list of strings, separated by spaces: ")
strings = a.split()

result = find_long_string(strings)

if result:
    print(f"The first string with length greater than 10 is: {result}")
else:
    print("No string with length greater than 10 was found.")'''
#8.Write a Python program that prompts the user to enter two file names and copies the contents of the first file to the second file. Handle the IOError exception and print an appropriate message if either of the files is not found.
'''def copy_file_contents():
    try:
        a = input("Enter the name of the source file: ")
        b = input("Enter the name of the destination file: ")
        with open(a, 'r') as src:
            content = src.read()
        with open(a, 'w') as dest:
            dest.write(content)
        print(f"Contents of '{a}' have been copied to '{b}'.")
    except IOError as e:
        print(f"An error occurred: {e}")
        print("Please check if the files exist and are accessible.")
copy_file_contents()'''
#9.Write a Python function that takes a string as input and returns the reverse of the string. Handle the TypeError exception and return None if the input is not a string.
'''def reverse_string(st):
    try:
        return st[::-1]
    
    except TypeError:
        print("Error: The input is not a string.")
        return None
result = reverse_string(input("Enter a string: "))

if result is not None:
    print(f"The reversed string is: {result}")'''
#10.Write a Python program that takes two integers as input and calculates their quotient and remainder. Handle the ValueError exception and print an appropriate message if the user enters non-integer inputs.
'''try:
    numerator = int(input("Enter the numerator (integer): "))
    denominator = int(input("Enter the denominator (integer): "))
    quotient = numerator // denominator
    remainder = numerator % denominator
    print(f"Quotient: {quotient}, Remainder: {remainder}")
except ValueError:
    print("Error: Invalid input. Please enter integer values only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")'''
#11.Write a Python function that takes a list of integers as input and returns the product of all the numbers in the list.
#Handle the ZeroDivisionError exception and return None if the input list contains a zero.
def product_of_list(numbers):
    try:
        if 0 in numbers:
            return None
        product = 1
        for num in numbers:
            product *= num
        
        return product
    except ZeroDivisionError:
        print("Error: The input list contains a zero. Product is undefined.")
        return None
    except TypeError:
        print("Error: Please provide a list of integers.")
        return None
a=[]
for i in range(int(input("Enter number of elements in list: "))):
    a.append(int(input("Enter a element: ")))
print(product_of_list(a))    

