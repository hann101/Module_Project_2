# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ManduItem(scrapy.Item):

    time = scrapy.Field()
    dealing = scrapy.Field()
    price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    num = scrapy.Field()