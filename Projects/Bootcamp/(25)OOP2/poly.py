class Animal():
    def speak(self):
        raise NotImplementedError('Subclass needs to implement this method!')


class Dog(Animal):
    def speak(self):
        return 'Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow!'


class Fish(Animal):
    pass


d = Dog()
print(d.speak())

# This code will give an error
# f = Fish()
# print(f.speak())

# The basic principle behind POLYMORPHISM is that a single object can take many forms!
# Here are 2 important Practical Applications of Polymorphism :
#   -> The same class (instance method) method works in a similar way for Different Classes
#   -> The same operation works for different kinds of objects
