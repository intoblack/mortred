# coding=utf-8
#!/usr/bin/env python

from scrapy import Spider
from scrapy.selector import Selector
from wenkr_spider.items import WenkrItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import Request
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from utils import SpiderUrlFilter


BLOOM_FILTER = SpiderUrlFilter().bloomfilter


class StockHeXun(Spider):

    name = "hexun"
    allowed_domains = ["stock.hexun.com"]
    child_link = re.compile(ur'http://stock.hexun.com/\d+-\d+-\d+/\d+.html')
    start_urls = [
        "http://stock.hexun.com/"]



    def __init__(self ,*arg, **kw):
        super(StockHeXun , self).__init__(*arg , **kw)
        self.link_extract = SgmlLinkExtractor()

    def parse(self, response):
        if response.url in self.start_urls:
            links = self.link_extract.extract_links(response)
            for x in links:
                match = self.child_link.match(x.url)
                if match:
                    if x.url not in BLOOM_FILTER:
                        BLOOM_FILTER.add(x.url)
                    yield Request(x.url, callback=self.parse)
        else:
            item = WenkrItem()
            title = response.xpath('//div[@id="artibodyTitle"]/h1/text()').extract()
            if len(title) == 0:
                title = response.xpath('//head/title//text()').extract()[0]
            else:
                title = title[0]
            item['title'] = title
            item['content'] = self.make_content(
                response.xpath('//div[@id="artibody"]//*//text()').extract())
            item['category'] = '股票'
            author = response.xpath('//span[@id="author_baidu"]/font/text()').extract()
            if len(author) > 0 :
                item['author'] = response.xpath('//span[@id="author_baidu"]/font/text()').extract()[0]
            else:
                item['author'] = u'和讯'
            item['tags'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
            if len(item['content']) > 80 :
                yield item

    def make_content(self, ps):
        print ps
        content = []
        for p in ps:
            if len(p) > 5 :
                content.append('  %s' % p)
        return '\r\n'.join(content)

    def __is_starts(self, word):
        for start in self.stop_contents:
            if word.startswith(start):
                return True
        return False
