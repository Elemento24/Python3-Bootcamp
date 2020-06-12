import re
text = 'Last night, Mrs. Daisy and Mr. White murdered Ms. Chow'

# Making Groups helps a lot in finding and replacing parts of a String
pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) (?P<name>[a-z])[a-z]+', re.I)

# Using sub method, which stands for Substitution, we can easily change parts of a String ...
# ... which matches the specified pattern
result = pattern.sub('REDACTED', text)
print(result)

# We can use combination of group from matches and our own text
# '\g' stands for group
result = pattern.sub('\g<1> REDACTED', text)
print(result)

# Or we can use just groups
result = pattern.sub('\g<1> \g<2>', text)
print(result)

# Also, we can specify Python identifiers and use them in sub method
result = pattern.sub('\g<1> \g<name>', text)
print(result)
