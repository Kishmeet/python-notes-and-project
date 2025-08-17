foods=[]
prices=[]
total=0

while True:
    food = input("enter food name or q to quit: ")
    if food.lower() == "q":
        break
    else :
     foods.append(food)
     price = float(input(f"enter price of {food}: $"))
     prices.append(price)
     total += price

print("----YOUR SHOPPING CART----")
for food in foods:
     print(food,end=" for $")
     print(prices[foods.index(food)])


print(f"total: ${total}")