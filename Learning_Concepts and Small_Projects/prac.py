'''
import string
small=string.ascii_lowercase
uppercase=string.ascii_uppercase
digits=string.digits
punctuation=string.punctuation
def passwordgen(length,seed):

    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ""
        for i in range(length):
            seed=(seed+69-143)*13+seed
            seed=seed%len(chars)
            password+=chars[seed]
        if validatepass(password):
            return password

def validatepass(password):
    l=any(x in password for x in small)
    u=any(x in password for x in uppercase)
    d=any(x in password for x in digits)
    p=any(x in password for x in punctuation)
    return l and u and d and p
print(passwordgen(int(input("Enter length of password: ")),int(input("Enter seed of password: "))))
if validatepass((input("Enter password: "))):
    print("Password is valid")
else:
    print("Password is not valid")
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i %5==0:
        print("Buzz")
    elif i%3==0 :
        print("Fizz")
    elif prime(i):
        print("prime")
    else:
        print(i)

def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input("Enter n: "))))

l=[]
n=int(input("Enter n: "))
for i in range(1,2*n+1):
    if i%2==0:
        l.append(i)
print(l)
for i in range(6):
    print(i*str(i))

s=input("Enter string: ")
a=input("Enter a letter  ")
b=input("Enter another letter  ")
n=""
for i in s:
    if i==a:
        n=n+b
    else:
     n=n+i
print(n)
def sum1(l:list):
    s=0
    for x in l:
        s=s+x
    return s

l=[]
while True:
    n=input("Enter number or any other character to quit : ")
    if n.isdigit():
        l.append(int(n))
    else:
        break
print(sum1(l))
def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j].upper()>arr[j+1].upper():
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
l=[]
n=int(input("Enter number of elements in String: "))
for i in range(1,n+1):
    l.append(input("Enter a String: "))
print(sort(l))
'''
from itertools import product

''''
l=[]
n=int(input("Enter number of elements in String: "))
for i in range(1,n+1):
    l.append(input("Enter a String: "))
l1=[]
n1=int(input("Enter number of elements in String: "))
for i in range(1,n1+1):
    l1.append(input("Enter  "))
l2=l+l1
print(list(set(l2)))
def largest(l):
    min=max=l[0]

    for i in l:
        if i>max:
            max=i
        if i<min:
            min=i
    smax=min
    for i in l:
        if  i>smax and i!=max:
            smax=i
    print(max,smax,min)
l=[]
n=int(input("Enter number of elements : "))
for i in range(1,n+1):
    l.append(int(input("Enter a number: ")))
largest(l)
def e(l):
    n=[]
    for i in l:
        if i%2==0:
            n.append(i)
    return n
l=[]
n=int(input("Enter number of elements : "))
for i in range(1,n+1):
    l.append(int(input("Enter a number: ")))
print(e(l))
def display(**info):
    for key , values in info.items():
        print(f"{key.capitalize()} : {values}")

d={}
d['name']=input("Enter name : ")
while True:
    key=input(f"Enter info for {d['name']}  : ").lower()
    if key!="done":
        d[key]=input(f"Enter {key}  : ")
    else:
        break
display(**d)
import string
import random
small=string.ascii_lowercase
cap=string.ascii_uppercase
digits=string.digits
punctuation=string.punctuation
def passwordgen(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ""
        for i in range(length):
            password+=chars[random.randint(0,len(chars)-1)]
        if validatepass(password):
            return password
def validatepass(password):
    l=any(x in password for  x in small)
    u=any(x in password for x in cap)
    d=any(x in password for x in digits)
    p=any(x in password for x in punctuation)
    return l and u and d and p
print(passwordgen(int(input("Enter length of password: "))))

s=input("Enter string: ")
sub=input("Enter substring: ")
count=0
for i in range(len(s)-len(sub)+1):
    if s[i:i+len(sub)]==sub:
        count=count+1
print(count)

s=input("Enter string: ")
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
s=input("Enter string: ")
words=s.split()
uniquewords=set(words)
print(len(uniquewords))

n=int(input("Enter a number  "))
a=n
order=len(str(a))
sum=0
while a>0:
    sum+=(a%10)**order
    a//=10
print(sum==n)
n=int(input("Enter a number  "))
a=0
b=1
c=0
for i in range(n):
    print(a)
    c=a+b
    b=a
    a=c

n=int(input("Enter a number  "))
print("Palindrome" if n==int(str(n)[::-1]) else "NOT Palindrome")
#
n=0
while True:
    a = n
    order = len( str( a ) )
    sum = 0
    while a > 0 :
        sum += (a % 10) ** order
        a //= 10
    if sum == n:
      print(n)
    n=n+1

year=int(input("Enter year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("YES")
else:
    print("NO")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while(1):
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    if day==29 and days_in_month[1] != 29:
            print("Please Enter correct date!")
            break;

    day += 1

    if day > days_in_month[month - 1]:
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    print("Next date is:", year, "-", month, "-", day)
    break;
def flatten(l):
    x = []
    for i in l:
        if type(i) == list:
            x.extend(flatten(i))
        else:
            x.append(i)
    return x

print(flatten([1, [3, 4, [5, 6]]]))
y=lambda l:([x for x in l if x.startswith('a') ])
print(y(['a','2','3a','4','5','6','a7']))
from functools import reduce
y=lambda l:reduce(lambda a,b:a*b,l)
print(y([1,2,3,4,5,6]))
y=lambda s:''.join([x if x not in 'aeiouAEIOU' else '' for x in s])
print(y('kIshmeet'))
#y=lambda l:map(lambda d:{'name':d['name'],'age':d['age']+1},l)
y=lambda l:[{'name':d['name'],'age':d['age']+1} for d in l]
print(list(y([{'name':'kishmeet','age':18},{'name':'aman','age':2111}])))
y=lambda l:list(map(lambda x:len(x),l))
print(y(['kIshmeet','singh']))
y=lambda l:list(filter(lambda x:len(x)>4,l))
print(y(['a10000','2a','3','4','a5']))
print(list(map(lambda x:x+1,[1,2,3,3])))
s=input("Enter string: ")
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
def flatten(l):
    x=[]
    for i in l:
        if type(i) == list:
            x.extend(flatten(i))
        else:
            x.append(i)
    return x
print(flatten([[[1,2],3,3]]))
a=[1,6,7,8,9,2,3,111]
a.sort()
print(a[len(a)-1]-a[0])
def concat(*args):
    x=''
    for i in args:
        x+=i
    return x
print(concat("a","b","c","d","e"))
def intesct(*lists):
    result_set = set( lists[ 0 ] )  # Start with the set of the first list
    for lst in lists[ 1 : ] :
        result_set &= set( lst )  # Find the intersection with each subsequent list
    return list( result_set )  # Convert the result back to a list


print(intesct([1,2,3,3],[2,3,4]))
'''
func = lambda lst: (result := 1, *[result := result * x for x in lst])[-1]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("Product:", func(input_data))