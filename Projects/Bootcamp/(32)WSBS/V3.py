# In this, we will learn how to access Data in the elements that we will select
# Using get_text()  method, we can access the Inner text in an element
# Using name (not a method), we can get the name of the tag
# Using attrs on an element, we can get a Dictionary of all the Attributes of the element
# We can also access attribute values using brackets

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
    <li id="spe_cial" class="special">This list item is special.</li>
    <li class="special super-special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# As we can see that when the element doesn't have any text inside it, like the meta tag ... 
# get_text() doesn't give us an error, instead it just gives us nothing.

# Also, we can notice that, using attrs gives us a Dictionary with key 'class'
# And the value of this key is always a list, since an element can have more than 1 class

for el in soup.select('.special'):
    print(el.get_text())
    print(el.name)
    print(el.attrs)
    print(el.attrs['class'])
    print()

# As we mentioned, we can use attrs
el = soup.find('h3').attrs['data-example']
print(el)

# Or we can use the square bracket '[]' notation
el = soup.find('h3')['data-example']
print(el)
el = soup.find('div')['id']
print(el)
