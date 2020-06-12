# In this, we are going to see some examples of functions that use Regex
# We can use the same concept to extract and validate data, belonging to different forms

import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


# The above function, extracts phone number (only 1) from the data passed
# '\b' makes sure that there is a whitespace character, or starting/ending of a line, wherever used.
print(extract_phone('My number is 432 766-8127'))
print(extract_phone('My number is 432 766-8127222'))
print(extract_phone('432 766-8127 is always available'))
print(extract_phone('432 766-8127'))
print()


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    return match


# The above function, extracts all the phone numbers from a string and returns them in a List
print(extract_all_phones('My number is 545 852-5121 or call me that 216 512-9126'))
print(extract_all_phones('My number is something, that you will never get!'))
print()


def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False


# The above function checks if the passsed string, is a phone number or not
# '^' ensures that the data starts with the thing specified
# '$' ensures that the data ends with the thing specified
print(is_valid_phone('432 516-9162'))
print(is_valid_phone('432 516-9162 Hello'))
print(is_valid_phone('Hello 432 516-9162, ring ring!'))
print()


def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


# The above function does the same thing as the previous function, using a Different Method
# Instead of using ^ and $, it used the method fullmatch, which makes sure that the data passed ...
# ... has the data in specified format and nothing else
print(is_valid_phone('432 516-9162'))
print(is_valid_phone('432 516-9162 Hello'))
print(is_valid_phone('Hello 432 516-9162, ring ring!'))
print()
