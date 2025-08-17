def pairs(lis,target):
    lis.sort()
    r=len(lis)-1
    l=0
    while l<r:
        if lis[l]+lis[r]>target:
            r=r-1
        elif lis[l]+lis[r]<target:
            l=l+1
        else:
            print(f"Sum pairs are {lis[l]}&{lis[r]}")
            r=r-1
            l=l+1
l=[]
while 1:
    n=input()
    if n.isdigit():
       l.append(int(n))
    else:
        break
pairs(l,int(input("Enter the sum you want to find: ")))