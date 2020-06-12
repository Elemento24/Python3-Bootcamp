# Generators are Iterators
# Every generator is an Iterator but the other way is not true
# Generators can be created with generator functions or generator expressions

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# This is a Generator Function, which gives us a Generator
# The main difference between a function & a generator function, is that a function does the same ...
# ... thing always, whenever called, but a Generator Function, remembers the variable...
# ... which is yielded


counter = count_up_to(5)
print(counter)

counter = count_up_to(10)
print(next(counter))

print("\nThe output of for loop:")
for num in counter:
    print(num)

# Here, you can see that once we call the next on counter, it stores the value of count (yielded)
# Generator is an easy way to create an Iterator, it comes with dunder methods created

# help(counter)
# You can use the above code to see that the counter has __next__ and __iter__ methods ...
# ... already attached to them.
