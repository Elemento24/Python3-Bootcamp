print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(Enter Player's 1 Choice) : ")
p2 = input("(Enter Player's 2 Choice) : ")
print("SHOOT!")

if p1 == "rock" and p2 == "scissors":
    print("Player 1 wins!")
elif p1 == "rock" and p2 == "paper":
    print("Player 2 wins")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins!")
elif p1 == "paper" and p2 == "scissors":
    print("Player 2 wins!")
elif p1 == "scissors" and p2 == "paper":
    print("Player 1 wins!")
elif p1 == "scissors" and p2 == "rock":
    print("Player 2 wins!")
elif p1 == p2:
    print("It's a Tie!")
else:
    print("Something Went Wrong!")
