f = open('data1.txt')
print(f)

print(f.read())
print(f.read())

# We can open a file using open function, which requires at least one argument
# The one must argument to the open function is the file name
# Open returns a file object, which can be seen with 'print(f)'
# We can read a file object with read method, as can be seen above
# Python reads a file with the help of a Cursor
# When we read a file, the cursor is placed at the last, and so when we read it again ...
# ... it doesn't display anything.
