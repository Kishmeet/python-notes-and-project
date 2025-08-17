def summ(l):
    sum1=sum(l)
    n=len(l)+1

    return (n*(n+1)/2)-sum1
def num_xor(l):
    xor = 0
    e=0
    for x in l:
        xor ^= x
    for i in range (len(l)+2):
        e^=i
    return e^xor

l=[]
for i in range(int(input("ENTER THE LENGTH OF LIST"))):
    l.append(int(input("Enter the number: ")))
print(num_xor(l))
print(summ(l))