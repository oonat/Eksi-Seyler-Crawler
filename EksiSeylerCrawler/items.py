# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Entry(scrapy.Item):
    nick = scrapy.Field()
    entry_id = scrapy.Field()
    title = scrapy.Field()
    entry_text = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    read_stat = scrapy.Field()
    share_stat = scrapy.Field()
