operator=input("enter operator")
number1=int(input("enter number"))
number2=int(input("enter number"))
if operator=="+":
    print(number1+number2)
elif operator=="-":
    print(number1-number2)
elif operator=="*":
    print(number1*number2)
elif operator=="/":
     print(number1/number2)
else:
     print("invalid operator")