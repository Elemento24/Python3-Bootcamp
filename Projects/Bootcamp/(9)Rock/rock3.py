print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(Enter Player's 1 Choice) : ")
print("\n")
print("*** NO CHEATING ***\n\n"*20)
p2 = input("(Enter Player's 2 Choice) : ")
print("SHOOT!")

if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("P1 wins")
elif p1 == "paper" and p2 == "rock":
    print("P1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("P1 wins")
else:
    print("P2 wins")

# Though this code is much shorter, it has much less Error Checks
