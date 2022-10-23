import random
import time

user_number = input(
    "Enter 1 for rock \nEnter 2 for paper \nEnter 3 for scissors\n ")


list = [1, 2, 3]
random.choice(list)


if user_number == 1:
    print("The computer choose Rock")
    if random.choice(list) == 2:
        print("You lost the game")
    elif random.choice(list) == 3:
        print("You won the game")
    else:
        print("The game has been drawn")


elif user_number == 2:
    print("The computer choose Paper")
    if random.choice(list) == 2:
        print("The game has been drawn")
    elif random.choice(list) == 3:
        print("You lost the game")
    else:
        print("You won the game")

else:
    print("The computer choose Scissors")
    if random.choice(list) == 2:
        print("You won the game")
    elif random.choice(list) == 3:
        print("The has been Drawn")
    else:
        print("You Lost the game")
