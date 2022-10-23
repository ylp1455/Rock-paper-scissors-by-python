import random
import time

user_number = int(input(
    "Enter 1 for rock \nEnter 2 for paper \nEnter 3 for scissors\n "))


# list = [1, 2, 3]
# random.choice(list)

# rock > scissors
# rock < paper

# scissors > paper



if(user_number==1):
    usrInput = "rock"
elif(user_number==2):
    usrInput="paper"
elif(user_number==3):
    usrInput="scisors"
else:
    usrInput="invalid input"

list = ["rock","paper","scisors"]
computer=random.choice(list)
print("You Choosed ",usrInput," And Computer Choosed",computer)
if((usrInput=="rock" and computer=="rock") or (usrInput=="paper" and computer=="paper") or (usrInput=="scisors" and computer=="scisors") ):
    print("Game Draw")
elif(usrInput=="rock" and computer=="scisors"):
    print("You win")
elif(usrInput=="rock" and computer=="paper"):
    print("You loose")
elif(usrInput=="paper" and computer=="rock"):
    print("You win")
elif(usrInput=="paper" and computer=="scisors"):
    print("You loose")
elif(usrInput=="scisors" and computer=="rock"):
    print("You loose")
elif(usrInput=="scisors" and computer=="paper"):
    print("You win")
else:
    print("Error")    






# if user_number == 1:
#     print("The computer choose Rock")
#     if random.choice(list) == 2:
#         print("You lost the game")
#     elif random.choice(list) == 3:
#         print("You won the game")
#     else:
#         print("The game has been drawn")


# elif user_number == 2:
#     print("The computer choose Paper")
#     if random.choice(list) == 2:
#         print("The game has been drawn")
#     elif random.choice(list) == 3:
#         print("You lost the game")
#     else:
#         print("You won the game")

# else:
#     print("The computer choose Scissors")
#     if random.choice(list) == 2:
#         print("You won the game")
#     elif random.choice(list) == 3:
#         print("The has been Drawn")
#     else:
#         print("You Lost the game")
