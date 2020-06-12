with open('data2.txt') as file:
    data = file.read()

print(file.closed)
print(data)

# The below code will give a value error
# print(file.read())

# For File I/O we can use 'with block'
# The advantage of using it, is that, it automatically closes the file ...
# ... as soon as the block gets terminated irrespective of what happens within the block ...
# ... like encountering an error or so.

# The basic behind-the-scenes working of with block is regarding the use of 2 ...
# ... dunder methods, __enter__ & __exit__
# We can define our own classes using with block by just defining both of the dunder methods
# As soon as the with block starts, it calls the __enter__ method
# And when the block ends, it calls the __stop__ method
