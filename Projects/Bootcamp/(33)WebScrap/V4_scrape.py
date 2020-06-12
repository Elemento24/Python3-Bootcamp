# The additional line of code 'res.encoding = "utf-8" ' after 'res = requests.get()' and the 2 ...
# ... additional parameters to open are used to tell the system, what encoding to Use.
# The default encoding the system uses, can't encode some characters

import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = 'http://quotes.toscrape.com'

# Used for scrapping the Quotes
def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        res = requests.get(f'{BASE_URL}{url}')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')

        quotes = soup.find_all(class_='quote')
        for quote in quotes:
            all_quotes.append({
                "text":quote.find(class_='text').get_text(),
                "author":quote.find(class_='author').get_text(),
                "bio-link":quote.find('a')['href']
            })

        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
        sleep(1)
    return all_quotes

# Write Quotes to CSV file
def write_quotes(quotes):
    with open('quotes.csv','w',encoding='utf-8',newline='') as file:
        headers = ['text', 'author', 'bio-link']
        csv_writer = DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)
