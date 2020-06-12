from csv import reader, writer

# The first approach, where only one file is opened at a Time
with open('fighter.csv') as file:
    csv_reader = reader(file)
    # Data is converted to a list, and saved into a variable
    fighters = [[s.upper() for s in row] for row in csv_reader]

with open('bolded.csv', 'w') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)


# The second approach using nested 'with' statements
with open('fighter.csv') as file:
    csv_reader = reader(file)
    with open('bolded.csv', 'w') as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])


# If we will use the below code, it will give us a ValueError
# Cause as soon as the first 'with' block is terminated, the fighter.csv file is closed
# And so, when we try to access csv_reader, it gives us an error, as the csv_reader ...
# ... was linked to fighter.csv which is closed

# with open('fighter.csv') as file:
#     csv_reader = reader(file)
# with open('bolded.csv', 'w') as file:
#     csv_writer = writer(file)
#     for fighter in csv_reader:
#         csv_writer.writerow([s.upper() for s in fighter])
