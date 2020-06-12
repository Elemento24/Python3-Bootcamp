from random import randint

# user = "y"

# while user == "y":
#     random_number = randint(1, 10)
#     num = int(input("\nGuess a number b/w 1 and 10 - "))
#     while num != random_number:
#         if num < random_number:
#             num = int(input("You guessed too low! Guess Again - "))
#         elif num > random_number:
#             num = int(input("You guessed too high! Guess Again - "))
#     print("You guessed it right!")
#     user = input("Do you want to play again! (y/n) - ")

# print("\nThank You for playing!")

random_number = randint(1, 10)

while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = randint(1, 10)
            guess = None
        else:
            print("\nThank You for playing!")
            break
