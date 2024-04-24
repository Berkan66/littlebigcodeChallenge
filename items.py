import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    authors = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
