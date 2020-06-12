class Animal:
    cool = True

    def make_sound(self, sound):
        print(f'This animal says {sound}')


class Cat(Animal):
    pass


blue = Cat()
blue.make_sound('Meow!')

print(blue.cool)
print(Animal.cool)
print(Cat.cool)

print(isinstance(blue, object))
print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
