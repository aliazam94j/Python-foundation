import random

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)


while player not in options:
    player = input("Enter your choice(Rock,Papper,Scissors) ").lower()


print(f"player: {player}")
print(f"computer: {computer}")


if player == computer:
    print("it is a tie")
elif player == "rock" and computer == "scissors":
    print("you win")
elif player == "paper" and computer == "rock":
    print("you win")
elif player == "scissors" and computer == "paper":
    print("you win")

else:
    print("computer wins!")

