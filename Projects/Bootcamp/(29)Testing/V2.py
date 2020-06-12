# We can write tests for functions inside of the Docstring
# They got quite a handful of syntax, which makes them hard to code in
# We must take care of whitespaces
# Also, in doctests, the order of keys in a Dictionary matters, whereas there is no such thing in code
# Also, it clutters up our function code and lacks many features of larger testing tools.

def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100,200)
    300
    """
    return a+b


def double(values):
    """ Double the Values in a List

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']

    >> double([True,None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2*element for element in values]
