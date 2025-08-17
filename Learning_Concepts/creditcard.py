# Python credit card validator program
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid
sum_odd_digits = 0
sum_even_digits = 0
#STEP 1
credit_card=input("Enter the credit card number: ")
credit_card=credit_card.replace("-","").replace(".","").replace(" ","")
credit_card=credit_card[::-1]
#STEP 2
for i in credit_card[::2]:
    sum_odd_digits += int(i)
for i in credit_card[1::2]:
    x=int(i)*2
    if x>=10:
        sum_even_digits +=(1+(x%10))
    else:
        sum_odd_digits += x
#Step 5
total=sum_odd_digits+sum_even_digits
if total%10==0:
    print("Credit Card Number is valid:",credit_card[::-1])
else:
    print("Credit Card Number is invalid:",credit_card[::-1])