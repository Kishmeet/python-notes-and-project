"""#Q1 Write a Python program that takes an integer as input and classifies it into one of the following categories:
"Perfect Number": If the sum of its proper divisors (excluding itself) is equal to the number.
"Abundant Number": If the sum of its proper divisors is greater than the number.
"Deficient Number": If the sum of its proper divisors is less than the number.
"Prime Number": If the number is prime.
"Composite Number": If the number is composite (not prime).
def classify_number(n):
    if n <= 1:
        return "Neither Prime nor Composite"

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def proper_divisors_sum(x):
        divisors = [1]
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                divisors.append(i)
                if i != x // i:
                    divisors.append(x // i)
        return sum(divisors)

    if is_prime(n):
        return "Prime Number"

    proper_sum = proper_divisors_sum(n)

    if proper_sum == n:
        return "Perfect Number"
    elif proper_sum > n:
        return "Abundant Number"
    else:
        return "Deficient Number"

    if n > 1:
        return "Composite Number"
        
# Get user input and classify the number
num = int(input("Enter an integer: "))
print(classify_number(num))
"""
"""#2.Create a program that generates a random password of a specified length. Must include a mix of uppercase letters, lowercase letters, numbers, and special characters. 
#The program shall also be able to validate a user provided password based on the must include list.

CAPITAL_ASCII_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ASCII_LETTERS = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
PUNCTUATIONS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def generate_password(length: int, seed: int) -> str:
    LEGAL_VALUES = CAPITAL_ASCII_LETTERS + ASCII_LETTERS + DIGITS + PUNCTUATIONS

    while True:
        password = ""
        for i in range(length):
            seed = (seed + 1) + (seed * 10)
            seed = seed % len(LEGAL_VALUES)
            password += LEGAL_VALUES[seed]

        if validate_password(password):
            return password

def validate_password(password: str) -> bool:
    capital_check = any(x in password for x in CAPITAL_ASCII_LETTERS)
    small_check = any(x in password for x in ASCII_LETTERS)
    digits_check = any(x in password for x in DIGITS)
    punctuations_check = any(x in password for x in PUNCTUATIONS)

    return all([capital_check, small_check, digits_check, punctuations_check])

choice = int(input("Would you like to [1] generate a password, or [2] validate a password?  "))

if choice == 1:
    length = int(input("Enter length: "))
    seed = int(input("Enter a number: "))
    print("Your password: ", generate_password(length, seed))
elif choice == 2:
    password = input("Enter password: ")
    if validate_password(password):
        print("This is a valid password!")
    else:
        print("This is not a valid password!")
else:
    print("Invalid choice")



#3.Modify the classic FizzBuzz problem. Print the numbers from 1 to 100, but for multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for numbers that are
#multiples of both 3 and 5, print "FizzBuzz." Additionally, for prime numbers, print "Prime."
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for a in range(1,101):
    if(a%3==0 and a%5==0):
        print("Fizzbuzz")

    elif(a%3==0):
         print("Fizz")

    elif (a % 5 == 0):

            print("Buzz")

    elif(is_prime(a)):
        print("Prime")
    else:
        print(a)
#4.How would you use a for loop to calculate the factorial of a number (e.g. 5! = 5 * 4 * 3 * 2 * 1)?
n=int(input("enter the number :"))
fact=1
if n==0:
    print("fact = 1")
else:
    for i in range(1,n+1):
        fact=fact*i
print("the factorial of the number is :",fact)


#5.How would you use a for loop to create a list of the first n even numbers?
n=int(input("Enter the number:"))
l=[]
for i in range(n*2):
    if i%2==0:
        l.append(i)
print("list of n")
print(l)


#6.How would you use a while loop to iterate through a range of numbers and print out only the odd numbers?
start =int(input("enter start number:"))
end = int(input("enter end number:"))
while start <= end:
    if start % 2 != 0:
        print(start)
    start+=1

#7. Create a program that prints a table of powers for a given number up to a specified exponent using a for loop.
n=int(input("Enter a number: "))
p=int(input("Enter power : "))
print("NUMBER | POWER | VALUE")
for i in range(1,p+1):
    print(str(n) + "      | " + str(i) + "     | " + str(n**i))

#Q8 Implement a program that printsthe following
# number pattern using nested for loops:
for i  in range(1,6):
    for j in range(0,i):
        print(i,end="")
    print("\n")

#9.How would you use a for loop to replace all occurrences of a certain letter in a string with a different letter?
s=input("Enter String: ")
s=list(s)
a=input("Enter character to replace: ")
r=input("Enter character to be used: ")
for  i in range(0,len(s)):
    if s[i]==a:
        s[i]=r
s="".join(s)
print("New String is: ",s)

"""
#10.Read a paragraph and print each word.
def print_words(paragraph: str) -> None:
    # Split the paragraph into words
    words = paragraph.split()
    
    # Print each word
    for word in words:
        print(word)

paragraph = input("ENTER")
print_words(paragraph)





































