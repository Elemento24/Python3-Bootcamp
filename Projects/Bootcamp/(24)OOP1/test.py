class User:

    # This is a Class Variable
    active_users = 0

    # This is a Class Method, that displays the number of Active Users
    @classmethod
    def display_active_users(cls):
        return f'There are currently {cls.active_users} active users!'

    # This is a Class Method, that returns an instance of User Class
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))

    # The __init__ function, whenever we create a new instance of the class
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    # Using this dunder method, we can print something, when we print out the Object Instance
    def __repr__(self):
        return f'{self.first} is {self.age}'

    # We define the method that logs out the user
    def logout(self):
        User.active_users -= 1
        return f'{self.first} logged out!'

    # We define a method, that returns of the full name of the User
    def full_name(self):
        return f'{self.first} {self.last}'

    # We define the method that returns the initials of the User
    def initials(self):
        return f'{self.first[0]}.{self.last[0]}.'

    # We define that returns a simple statement
    def likes(self, thing):
        return f'{self.first} likes {thing}'

    # Tells whether the User is Senior or not
    def is_senior(self):
        return self.age >= 65

    # Thsi method increases the age of the user
    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th birthday, {self.first}!'

# We always need to pass self as the parameter to a class method
# Otherwise, we will get an error


user1 = User('Joe', 'Blanca', 23)

# print(User.active_users)
# print(user1.first)
# print(user1.last)
# print(user1.age)
# print(user1.full_name())
# print(user1.initials())
# print(user1.likes('Ice Cream'))
# print(user1.is_senior())
# print(user1.birthday())
# print(user1.age)
# print(user1.logout())
# print(User.active_users)
print(User.display_active_users())

user2 = User.from_string('Tom,Jones,81')
print(user2)
print(user2.first)
print(user2.last)
print(user2.age)
