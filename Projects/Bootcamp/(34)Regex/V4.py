import re


def parse_name(input):
    name_regex = re.compile(
        r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$'
    )
    match = name_regex.search(input)
    print(match.group())
    print(match.group(2))
    print(match.group('first'))
    print(match.group(3))
    print(match.group('last'))


parse_name('Mrs. Tilda Swinton')

# When we need to access the value of a Group Match, we can either use Indices
# Or we can use Python Identifiers, which we can assign using the following Syntax ->
# '?P<label>' where we can use the 'label' to identify the Group Match
