item = input("what item did you buy?: ")
price = float(input("how much did you pay?: "))
quantity=int(input("how many did you buy?: "))
total = price * quantity
print(f"you have bought {quantity} X {item}/s for { round(total,2 )}")