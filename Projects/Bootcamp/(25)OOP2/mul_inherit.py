class Aquatic:

    def __init__(self, name):
        print('AQUATIC INIT!!')
        self.name = name

    def swim(self):
        return f'{self.name} is swimming!'

    def greet(self):
        return f'I am {self.name} of the Sea!'


class Ambulatory:

    def __init__(self, name):
        print('AMBULATORY INIT!!')
        self.name = name

    def walk(self):
        return f'{self.name} is walking!'

    def greet(self):
        return f'I am {self.name} of the Land!'


class Penguin(Ambulatory, Aquatic):

    # We can notice that as of now, only Penguin & Ambulatory init(s) are called!
    # But if we comment out the super() and uncomment the other 2 statements...
    # ... , we will see that both the init(s) are called

    def __init__(self, name):
        print('PENGUIN INIT!!')
        super().__init__(name)
        # Aquatic.__init__(self, name)
        # Ambulatory.__init__(self, name)


pen1 = Penguin('Fluffy')
print(pen1.swim())
print(pen1.walk())

# Take a note, as to which greet is called
print(pen1.greet())

print(f'Fluffy is instance of Penguin: {isinstance(pen1,Penguin)}')
print(f'Fluffy is instance of Aquatic: {isinstance(pen1,Aquatic)}')
print(f'Fluffy is instance of Ambulatory: {isinstance(pen1,Ambulatory)}')
