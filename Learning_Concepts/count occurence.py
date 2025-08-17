s=input("enter any string")
s=s.split()
d={}

for i in s:
    if i not in d.keys():
        d[i]=0

    d[i]=d[i]+1
print(d)
