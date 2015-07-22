#coding=utf-8
#!/usr/bin/env python


from twisted.internet import reactor, defer
from scrapy.crawler import Crawler
from scrapy import log
from scrapy.utils.project import get_project_settings
from wenkr_spider.spiders.kr36 import Kr36
from wenkr_spider.spiders.stockhexun import StockHeXun

p = {}
spiders = [Kr36(**p) , StockHeXun(**p)]



@defer.inlineCallbacks
def crawl():
    for spider in spiders:
        crawler = Crawler(get_project_settings())
        crawler.configure()
        crawler.crawl(spider)
        yield crawler.start()
    reactor.stop()
crawl()
log.start()
reactor.run()
