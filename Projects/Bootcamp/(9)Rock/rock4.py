import random

# from random import randint
# Also, using the above Syntax, we can only import randint
# Then, we can say num = randint(0,2)

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("(Enter Your Choice) : ").lower()
num = random.randint(0, 2)
com = None

if(num == 0):
    com = "rock"
elif(num == 1):
    com = "paper"
elif(num == 2):
    com = "scissors"

print(f"The Computer Plays : {com}")
print("SHOOT!")

if player == com:
    print("It's a Tie!")
elif player == "rock":
    if com == "paper":
        print("The Player wins!")
    else:
        print("The Computer wins!")
elif player == "paper":
    if com == "rock":
        print("The Player wins!")
    else:
        print("The Computer wins!")
elif player == "scissors":
    if com == "paper":
        print("The Player wins!")
    else:
        print("The Computer wins!")
else:
    print("Please enter a Valid Input!")
