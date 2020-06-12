from random import random


# random() generates a Random Number between 0 & 1

def flip_coin():
    if random() > 0.5:
        return "HEADS!"
    else:
        return "TAILS!"


print(flip_coin())
