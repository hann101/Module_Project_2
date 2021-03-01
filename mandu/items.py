# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 아이템 설정

import scrapy


class ManduItem(scrapy.Item):
    # title = scrapy.Field()
    name =scrapy.Field()
    num = scrapy.Field()
    price = scrapy.Field()
    # day_range = scrapy.Field()
    lowest_price = scrapy.Field()
    highet_price = scrapy.Field()
    volume = scrapy.Field()
