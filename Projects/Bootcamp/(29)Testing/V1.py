# Assert (not functions) statements are used for testing purposes
# They take 2 arguements, though the second one is Optional
# The first argument is a condition and the second one is an error message
# If the condition is truthy the assert statement returns None
# Else, it returns an 'AssertionError', with the error message if specified
# The drawback to assert statements is that they can be ignored ...
# if we run our code with '-O' flag like 'python3 -O V1.py'
# -O (stands for optimized mode), and so it is not a reliable way for absolute error detection

# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, 'Both numbers must be positive!'
#     return x+y


# val = add_positive_numbers(1, 1)
# print(val)
# val = add_positive_numbers(1, -1)
# print(val)


def eat_junk(food):
    assert food in ['Pizza', 'Candy', 'Burger'], 'Food must be a Junk Food!'
    return f'NOM NOM NOM, I am eating {food}!'


food = input('Enter a food please: ')
print(eat_junk(food))
