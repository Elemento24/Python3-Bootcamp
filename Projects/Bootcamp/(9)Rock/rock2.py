print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(Enter Player's 1 Choice) : ")
print("\n")
print("*** NO CHEATING ***\n\n"*20)
p2 = input("(Enter Player's 2 Choice) : ")
print("SHOOT!")

if p1 == p2:
    print("It's a Tie!")
elif p1 == "rock":
    if p2 == "paper":
        print("Player 2 wins!")
    elif p2 == "scissors":
        print("Player 1 wins!")
elif p1 == "paper":
    if p2 == "rock":
        print("Player 1 wins!")
    elif p2 == "scissors":
        print("Player 2 wins!")
elif p1 == "scissors":
    if p2 == "paper":
        print("Player 1 wins!")
    elif p2 == "rock":
        print("Player 2 wins!")
else:
    print("Something went wrong!")
