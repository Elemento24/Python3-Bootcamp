# In this we will learn about REGEX compilation flags, which we can pass while compiling ...
# ... expressions of REGEX, like 'VERBOSE' & 'IGNORECASE'

import re

regex = re.compile(r"""
    ^([a-z0-9_\.-]+)    # First part  of Email
    @                   # Single @ sign
    ([0-9a-z\.-]+)      # Email provider
    \.                  # Single Period
    ([a-z\.]{2,6}$)     # com, org, net, etc
""", re.VERBOSE | re.IGNORECASE)

# When we need to pass mutiple flags, we need to pass them being separated with a '|'
# For passing VERBOSE, we can also use re.X, and for ignorecase, we can use re.I
# VERBOSE (also known as Extended) allows us to span our regex expression over many lines
# It neglects the whitespace characters, and if we want to include whitespace characters ...
# ... there is a way for it as well. Also, it allows us to write comments for different parts ...
# ... of our regex expressions
# With the help of IGNORECASE, we can make sure that it neglects the CASE of characters ...
# ... and we can just specify 'a-z' or 'A-Z'

match = regex.search('thomaS123@yahoo.com')
print(match.group())
print(match.groups())
