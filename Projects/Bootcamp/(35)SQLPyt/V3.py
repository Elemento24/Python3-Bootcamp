import sqlite3

conn = sqlite3.connect('my_friends.db')
c = conn.cursor()

people = [
    ("Roald","Amundsen",5),
    ("Rosa","Parks",8),
    ("Henry","Hudson",7),
    ("Neil","Armstrong",7),
    ("Daniel","Boone",3)
]

# When we are inserting Data in Bulk, we can use executemany method of sqlite3
c.executemany('INSERT INTO friends VALUES (?,?,?)',people)

# We can also use a for loop to insert Bulk Data
# However, it comes in handy, when we need to perform Additional Logic with the data ...
# ... like the code below, which we can't do with executemany method
average = 0
for person in people:
    c.execute('INSERT INTO friends VALUES (?,?,?)',person)
    average += person[2]
average = average/len(people)
print(average)

conn.commit()
conn.close()

