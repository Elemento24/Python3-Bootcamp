# In this, we will learn about Pickling
# The pickle module will serialzie the data, converting it into something called a ...
# ... bite stream. And then we can unpickle it, and get back the data.

# The downside of Pickling data is that we can't read the stored data without unpickling it
# Or in other words we can say, that it is Python Specific

import pickle


class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f'{self.name} is a {self.species}!'

    def make_sound(self, sound):
        print(f'This animal says {sound}')


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species='Cat')
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f'{self.name} plays with {self.toy}!')


Blue = Cat('Blue', 'Scottish Fold', 'String')

# with open('pets.pickle', 'wb') as file:
#     pickle.dump(Blue, file)

with open('pets.pickle', 'rb') as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    zombie_blue.play()
