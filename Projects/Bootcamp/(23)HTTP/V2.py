import requests

url = 'https://icanhazdadjoke.com/'

# 'text/html' is the default 'Accept' Header
# Most websites don't have support that lets you have plain text
# For instance, if we make the same request to google, we can still get the same HTML text

# response = requests.get(url, headers = {
#     'Accept': 'text/plain'
# })

response = requests.get(url, headers = {
    'Accept': 'application/json'
})

# reponse.text will now give me the data in a String
# But we can't access it, since it's a Giant String & not a dictionary
# print(response.text)
# print(type(response.text))

# json() is a method, which can take the response and convert it into Python
data = response.json()
# print(type(data))
# print(data)
print(data['joke'])
print(f'Status: {data["status"]}')
