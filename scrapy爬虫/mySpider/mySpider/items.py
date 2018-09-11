# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    itemId = scrapy.Field()
    parentId = scrapy.Field()
    name = scrapy.Field()
    skuName = scrapy.Field()
    price = scrapy.Field()
    property = scrapy.Field()
    img_src = scrapy.Field()
    comment_list = scrapy.Field()