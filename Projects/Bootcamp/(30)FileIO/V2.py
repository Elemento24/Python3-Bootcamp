file = open('data2.txt')

# As we saw, that once Python reads the file, it places the cursor at the end of the file
# To place the cursor at the desired position, we can use seek method
# If we pass 0 as the argument to seek method, it will place the cursor at the beginning of the file
print(file.read())
print(file.read())
print(file.seek(0))
print(file.read())
print(file.seek(15))
print(file.read())

# Readline method helps to read one line at a time
# It terminates as soon as it hit the next line, and so places the cursor at the next line
print(file.seek(0))
print(file.readline())
print(file.readline())
print(file.readline())

# Readlines gets all the lines in a file in form of a list, instead of a giant string
# And places the cursor at the end of the file
print(file.seek(0))
print(file.readlines())

# We should close the file, once we are done with it
# It helps to save the Computer Resources
# We can check if the file is closed or not, with the help of closed attribute
# And we can close a file with the help of close function
print(file.closed)
file.close()
print(file.closed)

# And if we perform any operation on the file, once we close it, it will give us a ValueError
print(file.read())

# If we open a file in Python first, and then we make the changes in a file and save it...
# ... then we don't need to re-open the file, we can make any changes directly.
# Once we open a file, it sets up a connection with our code, which gets terminated...
# ... when we close the file
