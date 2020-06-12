# In this, we will see some other assert Statements from unittest module
# For others, refer to the Documentation

from random import choice


def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError('is_healthy must be a Boolean Value!')
    ending = 'because YOLO!'
    if is_healthy:
        ending = 'because my body is a temple!'
    return f'I am eating {food}, {ending}'


def is_funny(person):
    if person == 'tim':
        return False
    return True


def laugh():
    return choice(('Lol', 'Haha', 'Tehehe'))
