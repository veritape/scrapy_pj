# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScrapyPjItem(Item):
    # define the fields for your item here like:
    # name = Field()
    j_idt = Field()
    uuid = Field()
    expediente = Field()
    downloaded_file = Field()
