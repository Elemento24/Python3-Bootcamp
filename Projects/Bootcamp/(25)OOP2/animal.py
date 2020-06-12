class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f'{self.name} is a {self.species}!'

    def make_sound(self, sound):
        print(f'This animal says {sound}')


class Cat(Animal):

    # We can also call the __init__ method on the Base / Parent class as well
    # But in that case we need to pass self as an Argument

    def __init__(self, name, breed, toy):
        super().__init__(name, species='Cat')
        # Animal.__init__(self, name, species='Cat')
        self.breed = breed
        self.toy = toy

    def play(self):
        return f'{self.name} plays with {self.toy}!'


blue = Cat('Blue', 'Scottish Fold', 'String')
print(blue)
print(blue.play())
