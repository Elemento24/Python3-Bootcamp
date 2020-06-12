import sqlite3
conn = sqlite3.connect('my_friends.db')
c = conn.cursor()

# If we want to get all the data from the DB, we can just iterate over c, where c is an ...
# ... sqlite3 iterable object
# c.execute('SELECT * FROM friends')
# print(c)
# for friend in c:
#     print(friend)

# If we want to get all the data, we can also use fetchall method, which returns us a list of all the ...
# ... matching data, according to the Query that we pass in 'c'
# c.execute('SELECT * FROM friends')
# print(c.fetchall())

# If we want to get a single item, from the matching data, we can use fetchone method
# c.execute('SELECT * FROM friends WHERE first_name IS "Rosa" ')
# print(c.fetchone())

# We can also order our data according to a field using 'ORDER BY <column_name>'
c.execute('SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness')
print(c.fetchall())

conn.commit()
conn.close()