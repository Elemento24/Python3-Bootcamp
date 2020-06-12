print("How many kilometers, did you cycle today?")

# The input takes data in the form of a String
kms = input()
miles = float(kms) / 1.60934

# Round takes 2 parameters, the first being the thing to round
# And the second being the number of Decimal Digits
miles = round(miles, 2)
print(f"Your {kms}km ride is {miles}mi ")
