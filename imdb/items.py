# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    year = scrapy.Field()
    genre = scrapy.Field()
    tv = scrapy.Field()
    length = scrapy.Field()
    url = scrapy.Field()
