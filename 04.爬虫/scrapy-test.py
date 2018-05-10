# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print response.xpath('//a/text()').extract_first()

        for link in response.xpath('//a/@href').extract():
            yield {
                'link': link
            }