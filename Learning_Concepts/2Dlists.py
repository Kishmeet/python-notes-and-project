#fruits=    ["apple","banana","cherry","kiwi"]
#vegetables=["carrot","potato","tomato"]
#meats=     ["pork","beef","chicken"]
#groceries=[fruits,vegetables,meats]
groceries=[["apple","banana","cherry","kiwi"],
           ["carrot","potato","tomato"],
           ["pork","beef","chicken"]]
print(groceries)
print(groceries[0])
print(groceries[0][2])
print(groceries[1][1])

for collertion in groceries:

    for item in collertion:
        print(item,end=" ")

    print()