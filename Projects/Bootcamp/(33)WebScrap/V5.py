# In this we will be learning, how to use Scrappy (A Python Framework)
# It is a powerful tool, that helps us to make requests to websites, scrapes the data from the ...
# ... webpages and then helps to write them into csv files.

# The only downside of using it, is that it is a framework, so just like other frameworks ...
# ... we need to follow a bit of syntax, but then we will have a tool that can help us ...
# ... in doing intense web-scraping 

# It is very hard to write all the things for this. Must saw the video and refer to the docs

import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css('.price_color::text').extract_first(),
                'title': article.css('h3 > a::attr(title)').extract_first()
            }
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)
