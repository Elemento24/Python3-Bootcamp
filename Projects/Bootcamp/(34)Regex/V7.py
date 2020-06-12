import re

titles = [
    'Significant Others (1987)',
    'Tales of the City (1978)',
    'The Days of Anna Madrigal (2014)',
    'Mary Ann in Autumn (2010)',
    'Further Tales of the City (1982)',
    'Babycakes (1984)',
    'More Tales of the City (1980)',
    'Sure of You (1989)',
    'Michael Tolliver Lives (2007)'
]

# If we sort it now, it will just sort according to Lexographical Order
titles.sort()
print(titles)

fixed_titles = []
pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')

# We can also use Indices
for title in titles:
    # result = pattern.sub('\g<2> - \g<1>',title)
    result = pattern.sub('\g<date> - \g<title>', title)
    fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)

# As we can see that while defining the pattern, we have added a Space, after the title
# Otherwise, there will be a space at the end of the group title, which will leave ...
# ... a space, when we will substitute the parts.
