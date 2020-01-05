#The most basic example of using Scrapy, nothing special

import scrapy

class SpiderScrapy(scrapy.Spider):

    name = 'MySpider'
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):

        for quote in response.css('div.quote'):

            yield {
                'text':
                    quote.css('span.text::text').extract_first(),
                'author':
                    quote.css('small.author::text').extract_first(), }
