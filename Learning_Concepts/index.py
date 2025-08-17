#[start : end : step]
cr="1234-5678-9012-3456"
print(cr[1])
print(cr[:4])
print(cr[4:8])
print(cr[8:])
print(cr[::2])#every 2nd character from begining

print(cr[::-1])#reverse
print(cr[-2])
last_digits=cr[-4:]
print(last_digits)
a=input("Enter :")
print(a[::-1])