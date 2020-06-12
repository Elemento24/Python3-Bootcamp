# With the help of 're' module, we can use REGEX expressions in Python

import re

# A note about compile method, we don't need to use compile the Regex Pattern
# We can just pass it in all the methods instead of compiling it.
# But the downside of that, it will need to be compiled at every time, unlike this one ...
# ... where it will be compiled only one time.
# We can directly do "res = re.search(r'\d{3} \d{3}-\d{4}','Call me at 123 456-7890')"

# A note about the r flag, we pass it to methods, it stands for Raw String
# It helps us to use special characters like '\' without following any additional syntax
# Otherwise for using '\d' we would have to use '\\d'
# In short, always, pass the r flag to the methods

pattern = re.compile(r'\d{3} \d{3}-\d{4}')
print(type(pattern))
print()

# If we use search method, if no match is found, it returns None
res = pattern.search('12345 abcd')
print(res)
print()

# If we use findall method, if no match is found, it returns an Empty List
res = pattern.findall('12345 abcd')
print(res)
print()

# Search method returns a match object, and to get the data, we can use group method
res = pattern.search('Call me at 123 456-7890')
print(res.group())
print(res)
print()

# Findall method returns us a list, and we don't need to use any Additional Method
res = pattern.findall('Call me at 123 456-7890')
print(res)
print()

# If there are more than 1 match, and if we use search method, we still only get 1 item
res = pattern.search('Call me at 123 456-7890 or 909 213-3761')
print(res.group())
print(res)
print()

# Findall method, returns all the matches in a list
res = pattern.findall('Call me at 123 456-7890 or 909 213-3761')
print(res)
print()
