class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # We can define methods to return and set the age, thereby avoiding negative age
    # Or, we can use something known as 'property'

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    # What does property decorator do, is that, it kind of makes this property as an Attribute

    # This is a getter function
    @property
    def age(self):
        return self._age

    # This is a setter function
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('Age can"t be negative!')

    # This is another getter function
    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    # This is another Setter function
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')


Jane = Human('Jane', 'Goodall', 34)

# What we would do in case of Methods
# print(Jane.get_age())
# Jane.set_age(45)
# print(Jane.get_age())

# What we would do in case of property
# We can notice that we don't need to use parenthesis while accessing the properties
# This is due to the decorator 'property'
print(Jane.age)
Jane.age = 20
print(Jane.age)
print(Jane.full_name)
Jane.full_name = 'Howard Wolowitz'
print(Jane.__dict__)
print(Jane.full_name)
