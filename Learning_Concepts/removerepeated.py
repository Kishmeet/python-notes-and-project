str=input("enter string:")
str=str.split()
word=input("enter word:")
n=int(input("enter number of occurence of words to remove:"))
count=0
for i in range(len(str)):
    if str[i] == word:
        count=count+1
    if count==n:
         del(str[i])

print(str)
