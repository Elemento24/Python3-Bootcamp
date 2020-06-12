# In this, we will learn how to use jsonpickle
# jsonpickle stores our custom objects in JSON form
# Though it takes up more space as compared to pickle files, but once we store our ....
# ... data inside a JSON file, we can pass the data to other languages and programs ...
# ... where we can parse it and use it

import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# c = Cat('Charles', 'Tabby')

# with open('cat.json', 'w') as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

with open('cat.json') as file:
    content = file.read()
    unfrozen = jsonpickle.decode(content)
    print(unfrozen)
    print(unfrozen.name)
    print(unfrozen.breed)
