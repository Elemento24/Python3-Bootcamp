age = int(input("What's your age - "))
# 2-8, $2 ticket
# 65, $5 ticket
# $10 for everyone else

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You have to pay $10! ")
else:
    print("You are a Child/Senior! ")
