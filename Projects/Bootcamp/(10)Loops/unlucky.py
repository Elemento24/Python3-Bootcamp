for x in range(1, 21):
    if x == 4 or x == 13:
        state = "UNLUCKY"
    elif x % 2 == 0:
        state = "EVEN"
    else:
        state = "ODD"
    print(f"{x} is {state}")
