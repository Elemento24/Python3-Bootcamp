# In this part, we will study about Higher Order Functions
# These are bascially functions, which accept other functions as their arguments
# Or they return some function

from random import choice


def sum(n, func):
    total = 1
    for num in range(1, n+1):
        total += func(num)
    return total


def square(x):
    return x*x


def cube(x):
    return x**3


# In the above case, we saw that we can functions as arguments to other functions
print(sum(5, square))
print(sum(5, cube))


def greet(person):
    def get_mood():
        msg = choice(('Hi there ', 'Go away ', 'I love you '))
        return msg
    result = get_mood() + person
    return result


# In the above case, we can see that we can nest functions inside one another
print(greet('Aditi'))


def make_laugh_func():
    def get_laugh():
        l = choice(('Hahaha', 'Lol', 'Tehehe'))
        return l
    return get_laugh


# In the above case, we can see that we can return functions from other functions
laugh = make_laugh_func()
print(laugh())


def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('Hahaha', 'Lol', 'Tehehe'))
        return f'{laugh} {person}'
    return get_laugh


# In the above case, we can see that the Inner function, can access outer function scope
laugh_at = make_laugh_at_func('Myself')
print(laugh_at())
