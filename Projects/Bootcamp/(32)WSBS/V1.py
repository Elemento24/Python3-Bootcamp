# Using Beautiful Soup, we can parse HTML & XML
# It's an external module, that we need to install
# A very important note about beautiful soup, it doesn't enable us to get the HTML
# We can use requests module to get the html from a webpage
# As of now, we are just using a random HTML string

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

# We need to pass the HTML string, and the second string as 'html.parser', if we want to parse HTML
soup = BeautifulSoup(html, "html.parser")

# We can print the entire HTML, and it is a BeautifulSoup object
# print(soup)
# print(type(soup))

# We can also pring certain HTML tags using the following method
# But if there are more than one tag of the same type, then it will give us the first tag only
# print(soup.body)
# print(soup.body.div)

# We can also use the .find() method, to first a single tag of a type
# d = soup.find('div')
# print(type(d))

# We can use .find_all() if we want to get all tags of a type
# It will return a list of all tags that match the passed tag
# d = soup.find_all('div')
# print(d)

# We can also get an element by using an ID, and since we mostly have a single element on the ...
# ... entire page, with a given ID, so we don't need to use find_all()
# d= soup.find(id='first')
# print(d)

# We can also find all the elements using a class, and since there can be more than 1 element with ...
# ... a common class, we should use find_all(), in which we can pass the class as key-vaue pair ...
# ... under the key class_
# d = soup.find_all(class_='special')
# print(d)

# We can also find an element using Data Attributes
d = soup.find_all(attrs={'data-example':'yes'})
print(d)
