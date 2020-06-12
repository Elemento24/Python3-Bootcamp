import sqlite3

conn = sqlite3.connect('my_friends.db')
c = conn.cursor()

# With the help of triple quotes, we can span our SQL statement over many lines
# However, we rarely use this syntax, cause most of the times, we will be inserting ...
# ... the values of variables inside our Database
# query = '''INSERT INTO friends
#            VALUES ('Merriwether','Lewis',7)'''
# c.execute(query)

# We can also insert only data into 1 column, if we want to
# Here, we are using f strings to store the data of variables inside our DB
# However, this is not recommended, which will be explained with SQL injection
# first = 'Dana'
# query = f'INSERT INTO friends (first_name) VALUES ("{first}")'
# c.execute(query)

# The following is a better way to store the data of variables inside our DB
# We use '?' to represent our variables, and then, when we call the execute method, we pass ...
# ... a tuple of all our variables, so if there is a single variable, we must put a ',' 
# first = 'Mary-Todd'
# query = 'INSERT INTO friends (first_name) VALUES (?)'
# c.execute(query,(first,))

data = ('Steve','Irwin',9)
query = 'INSERT INTO friends VALUES (?,?,?)'
c.execute(query,data)

conn.commit()
conn.close()