import json


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


C = Cat('Charles', 'Tabby')

# Using the built-in-module json, we can convert Data into JSON form
# And then we can store it in a file that can be shared
j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)

# However, the json module works with the built-in-objects and to make it work with custom ...
# ... objects, it requires a lot of work
# Though we can use the dunder method __dict__ to convert our cutsom objects in a Dictionary ...
# ... and then use json module to store the data
k = json.dumps(C.__dict__)
print(k)

# Or we can use an external module called jsonpickle with stores our custom objects in JSON form
