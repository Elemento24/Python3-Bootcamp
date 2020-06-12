from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Human Named {self.first} {self.last} aged {self.age}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human('Newborn', self.last, 0)
        return 'You can"t add that!'

    # We use copy method, to make sure that we are creating copies of the Human in actual
    # If we won't use copy method, we will have multiple copies, but all of them will point ....
    # ... at the same human. So, if we make any change to one copy, all the copies will ...
    # ... reflect the same change

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return 'Can"t multiply that!'


J = Human('Jenny', 'Larsen', 47)
K = Human('Kevin', 'Jones', 41)

print(J)
print(K)

print(J+K)
print(J*3)

Triplets = (J+K)*3
Triplets[1].first = 'Jenny'
print(Triplets)

# The basic idea behind these Dunder Methods is that we can add them to our own classes
# So that, we can use built-in-methods of Python, with our classes!
