rows=int(input("enter rows: "))
coloumns=int(input("enter columns: "))
symbol=input("enter symbol: ")
for y in range(rows):
    for x in range(coloumns):
        print(symbol,end="")#for same line
    print()