# In this, we will learn how to implement Decorators having Arguments
# The basic idea behind them is that, they need an additional layer of ...
# function, when implementing their Decorator

# When we write:
#       @decorator
#       def func(*args, **kwargs):
#          pass
# We are really doing:
#       func = decorator(func)

# When we write:
#       @decorator_with_args(arg)
#       def func(*args, **kwargs):
#          pass
# We are really doing:
#       func = decorator_with_args(arg)(func)

from functools import wraps


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f'First arg needs to be {val}!'
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is('burrito')
def fav_foods(*foods):
    return foods


print(fav_foods('burrito', 'ice cream'))
print(fav_foods('ice cream', 'burrito'))


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2


print(add_to_ten(10, 12))
print(add_to_ten(1, 12))
