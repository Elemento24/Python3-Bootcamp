# In this, we are going to learn about one drawback of applying Decorators
# If we apply Decorator on a function, then we lose the metadata of the function ...
# ... on which we apply the decorator. The metadata of the wrapper function over-writes ...
# ... the metadata of the function, we are trying to Decorate
# It can be seen with add1 and log_function_data_1

# To preserve the metadata of the functions, we want to decorate we can use functools module
# The 'wraps' of 'functools' can be used to do the thing
# This is bascially a Decorator which we apply on our own wrapper function.

from functools import wraps


def log_function_data_1(fn):
    def wrapper(*args, **kwargs):
        '''I AM WRAPPER FUNCTION'''
        print(f'You are about to call: {fn.__name__}')
        print(f'Here is the Documentation: {fn.__doc__}')
        return fn(*args, **kwargs)
    return wrapper


def log_function_data_2(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''I AM WRAPPER FUNCTION'''
        print(f'You are about to call: {fn.__name__}')
        print(f'Here is the Documentation: {fn.__doc__}')
        return fn(*args, **kwargs)
    return wrapper


@log_function_data_1
def add1(x, y):
    '''ADDS TWO NUMBERS TOGETHER'''
    return x+y


@log_function_data_2
def add2(x, y):
    '''ADDS TWO NUMBERS TOGETHER'''
    return x+y


print(add1(10, 20))
print(add2(10, 20))

print(add1.__doc__)
print(add1.__name__)
print(add2.__doc__)
print(add2.__name__)

# help(add1)
# help(add2)
