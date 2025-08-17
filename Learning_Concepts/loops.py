num=int(input("enter a number"))
while num<1 or num>10:
    print("enter a number between 1 and 10")
    num=int(input("enter a number"))

print(f"you entered {num}")