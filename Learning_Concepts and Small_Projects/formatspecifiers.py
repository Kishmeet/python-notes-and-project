#format specifiers ={value :flags} format a value based on a what flags are inserted
# .(number)f=round to that many decimal places.
#:(number)= allocate that many spaces .
# :03=allocate and zero pad that many spaces.
#:<=left justify
#:>=right justify
#:^=center align
#:+=use a plus sign to indicate a positive value .
#:= = place sign to the left most position
#: = insert space between positive number
#:, = comma separator
price1 =3.4159
price2=-9870000.65
price3=12.34
print(f"price 1 is ${price1:+010}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+.1f}")