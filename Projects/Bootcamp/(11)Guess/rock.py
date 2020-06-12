from random import randint

print("\n...rock...")
print("...paper...")
print("...scissors...\n")

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
    print(f"\nPlayer Score : {player_wins} Computer Score : {computer_wins}")
    player = input("(Enter Your Choice) : ").lower()

    if player == "quit" or player == "q":
        break

    num = randint(0, 2)
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
            player_wins += 1
        else:
            print("The Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if com == "rock":
            print("The Player wins!")
            player_wins += 1
        else:
            print("The Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if com == "paper":
            print("The Player wins!")
            player_wins += 1
        else:
            print("The Computer wins!")
            computer_wins += 1
    else:
        print("Please enter a Valid Input!")

print("\nFINAL RESULT : ")
if player_wins == winning_score:
    print("The PLAYER wins!")
elif computer_wins == winning_score:
    print("The COMPUTER wins!")
else:
    print("It's a TIE!")
