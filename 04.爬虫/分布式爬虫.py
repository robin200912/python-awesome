# pip install scrapy-redis

# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class CrawlRedisSpiderSpider(RedisCrawlSpider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    redis_key = 'baidu:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r''), follow=True),
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        data = {
            'title': response.xpath('//title/text()').extract_first(),
        }
        return data
