# THE END POINT IS NEVER INCLUDED AS A PART OF RANGE

# We can also pass a single argument in range
# It will iterate from 0 till 7

for num in range(8):
    print(num)

# We can also pass a third paramter, which signifies the steps
# It will iterate for the odds in the given range

for num in range(1, 10, 2):
    print(num)

# Also, we can pass the third parameter as Negative
# It will signigy that we need to count backwards

for num in range(7, 0, -1):
    print(num)
