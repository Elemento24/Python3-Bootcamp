import sqlite3

# We use the below code to connect to a DB. If the file exists, then it will connect to the ...
# ... specified DB, else it will create the DB file
conn = sqlite3.connect('my_friends.db')

# Create a Cursor Object
# Cursor object, is basically a small amount of Storage Space, that we can use to store our DB
c = conn.cursor()

# Execute some SQL
c.execute('CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)')

# Commit the changes
conn.commit()

# We always need to close the connection, once we are done, just like we close a file
conn.close()
