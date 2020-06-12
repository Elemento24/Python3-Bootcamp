# In this we will see how to test our code using a built-in-module called unittest
# This is probably the easiest way to implement tests for Python Code
# Though we need to follow a little extra syntax, but if used correctly ...
# ... we have very powerful tools at our disposal.


def eat(food, is_healthy):
    ending = 'because YOLO!'
    if is_healthy:
        ending = 'because my body is a temple!'
    return f'I am eating {food}, {ending}'


def nap(num):
    if num >= 2:
        return f'Ugh I overslept. I did not mean to nap for {num} hours!'
    return 'I am feeling refreshed after my 1 hour nap!'
