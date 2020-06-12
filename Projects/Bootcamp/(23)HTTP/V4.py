import requests
from random import choice

print('Dad Joke 3000\n')
user_input = input('Let me tell you a joke! Give me a topic: ')

url = 'https://icanhazdadjoke.com/search'
data = requests.get(url,
    headers = {'Accept': 'application/json'},
    params = {'term': user_input}
).json()

length = data['total_jokes']
results = data['results']

if not length:
    print(f"Sorry, I don't have any jokes about {user_input}! Please try again.") 
elif length == 1:
    print(f"I've got one joke about {user_input}. Here it is:")
    print(results[0]['joke'])
else:
    print(f"I've got {length} jokes about {user_input}. Here's one:")
    print(choice(results)['joke'])
