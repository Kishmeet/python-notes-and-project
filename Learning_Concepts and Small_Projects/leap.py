year=int(input("Enter year to check for leap year: "))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("Leap year")
else:
    print("Not a leap year")