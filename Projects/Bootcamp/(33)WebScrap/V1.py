# The basic idea behind getting the Quotes on all the pages, is to find the next button on the Page
# And then making a request to that URL, and continue this process, till we can find a Next Button.

# The website used in this case is for Scraping Purposes, so we don't need to delay our requests.
# But if we want to scrap data from a website, that doesn't support Scraping, we should delay our ...
# ... requests, so that we don't get caught. For that, we can use sleep function from time module.

import requests
from bs4 import BeautifulSoup
from time import sleep

all_quotes = []
base_url = 'http://quotes.toscrape.com'
url = '/page/1'

while url:
    res = requests.get(f'{base_url}{url}')
    print(f'Now scraping {base_url}{url}....')
    soup = BeautifulSoup(res.text,'html.parser')

    quotes = soup.find_all(class_='quote')
    for quote in quotes:
        all_quotes.append({
            'text': quote.find(class_='text').get_text(),
            'author': quote.find(class_='author').get_text(),
            'bio_link': quote.find('a')['href']
        })

    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None
    # sleep(2)

print(all_quotes)
