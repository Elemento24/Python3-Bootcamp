# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f'Hi, I am {name}!'


@shout
def order(main, side):
    return f'Hi, I would like the {main}, with a side of {side}, please!'


@shout
def lol():
    return 'Lol!'


# If we will use the commented function for Decorating, it will give an error
# As the number of arguments in the functions we are decorating vary.
# The solution is using *args & **kwargs
print(greet('Tony'))
print(order('Burger', 'Fries'))
print(lol())
