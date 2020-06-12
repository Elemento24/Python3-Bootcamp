# In this, we will see how to use searching to navigate, that is using 'Methods'

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class='special'>
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
# When we use Attributes to Navigate, we can use find_parent() / find_parents() ...
# ... find_next_sibling() / find_next_siblings(), find_previous_sibling() / find_previous_siblings()

soup = BeautifulSoup(html, "html.parser")
print()

# Using the below method, we can find the next sibling, and it does give us the real sibling ...
# ... if it exists, that is, it ignores '\n' as a sibling
d = soup.find(id='first').find_next_sibling()
print(d)
print()

d = soup.find(id='first').find_next_sibling().find_next_sibling()
print(d)
print()

# Using find_next_siblings(), we can get a list of all the siblings of an element
d = soup.find(id='first').find_next_siblings()
print(d)
print()

d= soup.find(class_='super-special').find_next_sibling()
print(d)
print()

# We can also pass arguments to the methods like below, to select a particular sibling ...
# ... out of all the next siblings
d= soup.find(class_='super-special').find_next_sibling(class_='special')
print(d)
print()

# Using the below method, we can method previous sibling, ana it also ignores '\n'
d = soup.select('[data-example]')[1].find_previous_sibling()
print(d)
print()

# Using the below code, we can find out the parent of an element
d = soup.find('h3').find_parent()
print(d)
print()

d = soup.find('h3').find_parent('html')
print(d)
print()

# Using find_parents(), we can get a list of all the parent elements of a Tag, starting from the ...
# ... immediate parent till the '!DOCTYPE htmlclear'
d = soup.find('h3').find_parents()
print(d)
print()