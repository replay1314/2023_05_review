# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
    country = scrapy.Field()
    type = scrapy.Field()
