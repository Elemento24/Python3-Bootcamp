# Ask for age
age = input("How old are you - ")
if age:
    age = int(age)
    # 21+ Drink, Normal Entry
    if age >= 21:
        print("You are good to enter, and are allowed to Drink!")
    # 18-21, wristband
    elif age >= 18:
        print("You can enter, but need a Wristband!")
    # Too young, Sorry
    else:
        print("You can't come in, little one!")
else:
    print("You haven't entered any age! ")
