menu={"pizza":3.0,
      "nachos":2.0,
      "burger":2.5,
      "fries":1.5,
      "hotdog":3.0,
      "sandwich":2.0,
      "chicken":3.0,
      "soda":1.0,
      "coffee":1.5}
cart=[]
total=0
print("-----MENU------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("---------------")
while True:
    item=input("enter item name or q to quit: ").lower()
    if item=="q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        total+=menu[item]
print("----YOUR CART----")
for item in cart:
    print(f"{item} for ${menu[item]}")
print("\n------------------")
print(f"total: ${total:0.2f}")