import random

#random.seed(1)
"""
number=random.randint(low,high)
print(number)
n=random.random()
options=("rock","paper","scissors")
print(random.choice(options))
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)
"""
low=1
high=100
gusses=0
number=random.randint(low,high)
is_running=True
print("PYTHON NUMBER GUESSING GAME")
print(f"ENTER NUMBER BETWEEN {low} AND {high}")

while(is_running):
    guess=input("")
    if guess.isdigit():
        guess=int(guess)
        gusses+=1
        if guess<low or guess>high:
            print("Invalid input, try again!!")
            print(f"ENTER NUMBER BETWEEN {low} AND {high}")
        elif guess<number:
            print("Too low!!Try again")
        elif guess>number:
            print("Too high!!Try again")
        else :
            print(f"CORRECT! The number is {number} and you guessed it in {gusses} guesses!!")
            is_running=False
    else :
        print("Invalid input, try again!!")
print("-----------Game over----------")
