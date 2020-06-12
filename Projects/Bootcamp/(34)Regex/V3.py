import re

url_regex = re.compile(
    r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
)
match = url_regex.search('http://www.youtube.com/videos/colt/web-dev')

# With the help of group method, we can also access match group-wise
# group method in general shows the entire match
print(match.group())

# We can pass indices to group method, to have access to a particular group match
# Passing 0 index is as good as using group method without any index
# Index 1, basically refers to the first group, unlike 0 index, in general
print(match.group(0))
print(f'Protocol: {match.group(1)}')
print(f'Domain: {match.group(2)}')
print(f'Everything Else: {match.group(3)}')

# We can also use groups method, which gives us a tuple of all the Group Matches
print(match.groups())
