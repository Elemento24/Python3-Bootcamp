# In the previous version, we saw how to select elements using Tag Names
# Also, we saw how to select elements using find() and find_all() methods
# In this, we will learn how to use CSS to select elements

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# For using CSS to select elements, we will be using select() method
# One thing to note about select() method, is that, it always returns a List
# Using the below code, we can select elements using ID(s), Class(es) & Attribute(s)

d = soup.select('#first')
print(d)

d = soup.select('.special')
print(d)

d = soup.select('[data-example]') 
print(d)