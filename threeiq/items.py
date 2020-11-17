# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreeiqItem(scrapy.Item):
    Cashname = scrapy.Field()
    Cashvalue = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()

