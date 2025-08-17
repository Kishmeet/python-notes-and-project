import random
options=("rock","paper","scissor")
running=True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
     player=input("Enter a choice (Rock, Paper, Scissor)").lower()
    print(f"Computer choice: {computer}")
    print(f"Player choice: {player}")
    if player == computer:
        print("It's a Draw!!")
    elif player == "rock" and computer == "scissor":
        print("you win!!")
    elif player == "paper" and computer == "rock":
        print("you win!!")
    elif player == "scissor" and computer == "paper":
        print("you win!!")
    else :
        print("You lose!!")
    play_again=input("Do you want to play again? (y/n)").lower()
    if play_again != "y":
        running=False
print("Thank you for playing!")