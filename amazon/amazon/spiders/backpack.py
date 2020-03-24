# -*- coding: utf-8 -*-
import scrapy


class BackpackSpider(scrapy.Spider):
    name = 'backpack'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['http://www.amazon.cn/']

    def parse(self, response):
        pass
