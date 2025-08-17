'''
#1.Find a factorial of given number.

n=int(input("Enter a number: "))
f=1
a=n
while a>1:
    f=f*a
    a=a-1
print(f"Factorial of {n} is {f}")

#2.Find whether the given number is Armstrong number.
n=int(input("Enter a number: "))
order=len(str(n))
sum=0
temp=n
while temp>0:
    d=temp%10
    sum=sum+d**order
    temp=temp//10
if sum==n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

#3.Print Fibonacci series up to given term
n=int(input("Enter  number of terms: "))
a=0
b=1
c=0
for i in range(1,n+1):
    print(a,end=" ")
    c=a+b
    b=a
    a=c

#4.Write a program to find if given number is prime number or not.
c=0
n=int(input("Enter a number : "))
if n<2:
    print(f"{n} is Not a Prime Number")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
         c=1
    if c==0:
        print(f"{n} is Prime Number")
    else:
        print(f"{n} is not Prime Number")

#5.Check whether given number is palindrome or not.
n=int(input("Enter a number : "))
#a=str(n)
#a=int(a[::-1])
# or
a=0
temp=n
while temp>0:
    d=temp%10
    a=a*10+d
    temp=temp//10
if a==n:
    print(f"{n} is Palindrome Number")
else:
    print(f"{n} is not Palindrome Number")

#6.Write a program to print sum of digits.
n=int(input("Enter a number : "))
sd=0
temp=n
while temp>0:
    sd+=temp%10
    temp=temp//10

print(f"Sum of digits of {n} is {sd}")

#7.Count and print all numbers divisible by 5 or 7 between 1 to 100.
c=0
for i in range(1,101):
    if i%5==0 or i%7==0:
        c=c+1
        print(i,end=" ")
print(" ")
print(f"Count of Numbers divisible by 5 or 7 is {c}")

#8.Convert all lower cases to upper case in a string.
str=input("Enter a string: ")
new=""
for i in str:
    if ord(i)>=97 and ord(i)<=122:
        new+=chr(ord(i)-32)
    else:
        new+=i
print(f"New String is {new}")

#9.Print all prime numbers between 1 and 100.
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
            if n%i==0:
             return False
    return True
for i in range(2,101):
  if is_prime(i):
     print(i,end=" ")

#10.Print the table for a given number: 
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} * {i}  = {n*i}")

'''
