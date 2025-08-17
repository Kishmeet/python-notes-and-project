#typecasting=The process of converting a value of one data type to another
# Explicit
name = "kishmeet"
age = 17
distane=10.6
student=True
print(type(name))
print(type(age))
print(type(distane))
print(type(student))
age=float(age)
print(type(age))
distane=int(distane)
print(distane)
student=str(student)
print(student)
print(type(student))
name=bool(name)
print(name)

#IMPLICIT
x = 2
y = 2.0
x=x/y
print(x)