# coding=utf-8


from scrapy import Spider
from scrapy.selector import Selector
from wenkr_spider.items import WenkrItem
from scrapy import Request
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from utils import SpiderUrlFilter
BLOOM_FILTER = SpiderUrlFilter().bloomfilter


class Kr36(Spider):

    name = "kr36"
    allowed_domains = ["36kr.com"]
    child_link = re.compile(ur'/p/\d+\.html')
    start_urls = [
        "http://www.36kr.com"]

    stop_contents = {'原创文章',  'BAIDU_CLB_fillSlot'}


    def __init__(self ,*arg, **kw):
        super(Kr36 , self).__init__(*arg , **kw)


    def parse(self, response):
        filename = response.url.split('//')[1]
        if response.url in self.start_urls:
            for link in response.xpath("//a[contains(@class, 'title') and contains(@class, 'info_flow_news_title')]/@href").extract():
                url = '%s%s' % ('http://www.36kr.com', link)
                if url not in BLOOM_FILTER:
                   BLOOM_FILTER.add(url)
                   yield Request(url, callback=self.parse)
        else:
            item = WenkrItem()
            item['title'] = response.xpath(
                '//h1[@class="single-post__title"]/text()').extract()[0]
            item['content'] = self.make_content(
                response.xpath('//section[@class="article"]//*/text()').extract())
            item['category'] = '互联网'
            item['author'] = '36kr'
            item['tags'] = response.xpath('//meta[@name="keywords"]/@content').extract()[
                0].replace('，', ',').replace('cn-startups', '创业')
            yield item

    def make_content(self, ps):
        content = []
        for p in ps:
            if len(p) > 5 and not self.__is_starts(p):
                content.append('  %s' % p)
        return '\r\n'.join(content)

    def __is_starts(self, word):
        for start in self.stop_contents:
            if word.startswith(start):
                return True
        return False
