# dictionary= a collection of {key :values }pairs
#             ordered and changeable.No duplicates.
capitals={"USA":"Washington D.C.","India":"New Delhi","China":"Beijing","Russia":"Moscow"}
#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))
#print(capitals.get("Japan"))
#if capitals.get("Japan") :

 #   print("That capital exist in the dictionary")
#else:
 #   print("Capital does not exists in the dictionary")
#capitals.update({"Germany":"Berlin"})
#capitals.pop("USA")
capitals.popitem()
#capitals.clear()
#keys=capitals.keys()
#for key in capitals.keys():
 #  print(key)
#values=capitals.values()
#print(values)
#for value in capitals.values():
  #   print(value)
items=capitals.items()
print(items)
for keyset,valueset in items:
    print(f"{keyset}:{valueset}")
L=[1,2,3,4,5,6,7,8,9]
print({k : v for k,v in zip(capitals.keys(),L)})