import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Just creating a table by the name of 'users'
# query = 'CREATE TABLE users (username TEXT, password TEXT)'
# c.execute(query)

# Inserting a single user in the table
# data = ('Blue','Meow')
# query = 'INSERT INTO users VALUES (?,?)'
# c.execute(query,data)

u = input('Please enter your username -> ')
p = input('Please enter your password -> ')

# Now, if we are just interpolating the values of the variables, using a f-string ...
# ... a malicious user, may bypass the security to access our DB
# For instance, if he used a username, and in the password typed <" OR 1=1 -->, he could ...
# ... access the entire DB. To avoid this, we should not use f-strings.
# query = f'SELECT * FROM users WHERE username="{u}" AND password="{p}"'
# c.execute(query)

# Hence, the preferred way, is to use '?' and pass in the variables in the execute method
# They will take care of all these issues
query = 'SELECT * FROM users WHERE username=? AND password=?'
c.execute(query,(u,p))

result = c.fetchone()
if result:
    print('WELCOME BACK!')
else:
    print('FAILED LOGIN!')

conn.commit()
conn.close()
