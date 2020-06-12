# We generally don't use this method to Handle CSV files
# with open('fighter.csv') as file:
#     print(file.read())

# Instead we use functions from the built-in-module (CSV Module), reader & DictReader
# They are specially meant for handling CSV files
# Both reader & DictReader, gives us Iterators, that once we iterate over them, they get exhausted
# If we want to use the data in other places in our code, we can store them in other ...
# ... formats like lists, dictionaries

from csv import DictReader, reader

# The reader function allows us to iterate over rows of the CSV as Lists
with open('fighter.csv') as file:
    csv_reader = reader(file)
    for fighter in csv_reader:
        print(f'{fighter[0]} is from {fighter[1]}!')
        # print(fighter)

print('\n')

# The DictReader function allows us iterate over rows of the CSV as Ordered Dicts
# Ordered Dicts can be interpreted as Dictionaries in which the keys have an Order, unlike regualar ones
with open('fighter.csv') as file:
    csv_reader = DictReader(file)
    for fighter in csv_reader:
        print(fighter['Name'] + ' is from ' + fighter['Country'])
        # print(fighter)

print('\n')

# As we can see that DictReader doesn't print the header line, while Reader does print it
# To Avoid it, we can use the following code
with open('fighter.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f'{fighter[0]} is from {fighter[1]}!')
        # print(fighter)

# One added advanatge of Reader is that, it accepts a Delimiter Kwarg
# It helps to interpret the data, in case it isn't separated by commas
# We can use the statement -> csv_reader = reader(file, delimiter = '|'), for data separated by '|'
