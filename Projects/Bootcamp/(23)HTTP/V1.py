# With the help of requests module, we can make HTTP requests like get & post requests
# This helps us to interact with APIs, so that we can collect and use data from the web.
# Also, we can make requests to websites without API, but it would be a bit difficult ...
# ... to use in the code, so we mostly make requests to APIs.

import requests 

url = 'http://www.google.com'
response = requests.get(url)

print(f'You request to {url} come back with status code {response.status_code}')
print(response.text)