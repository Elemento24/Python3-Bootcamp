# In this, we will learn how to use Query String
# It is basically a way to pass data to the server as part of a GET request
# http://www.example.com/?key1=value1&key2=value2
# As we can seem '?' denotes the Query String, and the params are passed in key-value pairs
# Also, the key-value pairs are separated by '&'

# All the things about the API can be found out, reading the DOCS

import requests

url = 'https://icanhazdadjoke.com/search'

response = requests.get(url, 
    headers = { 'Accept': 'application/json'},
    params = {'term': 'cat', 'limit': 3}
)

data = response.json()
print(data['results'])

# We have 2 options when we need to pass a Query String

# Either we can manually construct the link and then pass it to request:
# response = requests.get('http://www.example.com?key1=value1&key2=value2')
# Or we can pass the key value pairs in form of a Dictionary, as can be seen in the code