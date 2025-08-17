principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("enter the principle amount: "))
    if principle<=0:
        print("principle cannot be negative or zero")

while rate<=0:
    rate=float(input("enter the rate of interest: "))
    if rate<=0:
        print("rate cannot be negative or zero")

while time<=0:
    time=int(input("enter the time period: "))
    if time<=0:
        print("time cannot be negative or zero")

total=principle*pow((1 + rate/100),time)
print(f"balance after {time} years is {total:.2f}")
