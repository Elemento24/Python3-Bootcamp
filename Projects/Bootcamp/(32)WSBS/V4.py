# Navigating refers to selecting Siblings, Child & Parent Elements
# There are 2 ways for Navigating, either ia tags or via searching
# In this, we will see how to use tags to navigate, that is using 'Attributes'

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
# When we use Attributes to Navigate, we can use parent/parents, contents ...
# ... next_sibling/next_siblings and previous_sibling/previous_siblings

soup = BeautifulSoup(html, "html.parser")
print()

# 'contents' gives us all the child tags of an element in a list, including '\n'
# When we are using attributes, we must consider '\n' as the elements of the List
# data = soup.body.contents
# print(data)
# print()

# We can use next_sibling, to select the next_sibling, however it considers '\n' as a sibling too
# data = soup.body.contents[1].next_sibling.next_sibling
# print(data)
# print()

# We can use parent to select the parent tag
# data = soup.find(class_='super-special').parent
# print(data)
# print()

# data = soup.find(class_='super-special').parent.parent
# print(data)
# print()

# next_siblings gives us a generator object of all the siblings of an element
# data = soup.find(class_='super-special').next_siblings
# print(data)
# data = list(data)
# print(data)
# print()

# parents gives us a generator object of all the parents of an element starting from the ...
# ... immediate parent till the '!DOCTYPE html'
data = soup.find(class_='super-special').parents
print(data)
data = list(data)
print(data)
print()