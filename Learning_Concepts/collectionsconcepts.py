#collections=single "variable" that are used to store multiple values
#lists =[] odered and changeable.Duplicates OK
#set={} unordered and immutable.but Add/Remove Ok.No Duplicates
#truple=() ordered and unchangeable .Dublicates Ok .Faster

#Lists........
#fruits = ["apple", "banana", "cherry","coconut"]
#print(dir(fruits))
#print(help(fruits))
#print(fruits)
#print(fruits[1])
#print(fruits[4])
#print(fruits[::-1])
#print(fruits[::2])
#for x in fruits:
 #   print(x)

#print(len(fruits))
#print("apple" in fruits)
#print("mango" in fruits)
#fruits[0]="pineapple"
#print(fruits)
#fruits.append("mango")#add element to the end of the lists
#fruits.remove("cherry")
#fruits.insert(1,"orange")
#fruits.sort()
#fruits.reverse()#reverse list
#fruits.clear()
#print(fruits.index("cherry"))
#print(fruits.count("cherry"))
#print(fruits)........................


#set............
#fruits={"apple","banana","cherry","coconut"}
#print(fruits)
#print("pineapple" in fruits)
#print(fruits[0])#TypeError: 'set' object is not subscriptable
#fruits.add("pineapple")
#fruits.remove("cherry")
#fruits.pop()generally removes first element but for sets remove random element
#fruits.clear()
#print(fruits).......................

#tuple.............
fruits=("apple","banana","cherry","coconut")
#print(fruits[0])
#print(len(fruits))
#print("Aa" in fruits)
#print(fruits.index("cherry"))
#print(fruits.count("cherry"))
#print(fruits)

#.........end........


