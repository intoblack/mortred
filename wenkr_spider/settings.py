# -*- coding: utf-8 -*-

# Scrapy settings for wenkr project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wenkr_spider'

SPIDER_MODULES = ['wenkr_spider.spiders']
NEWSPIDER_MODULE = 'wenkr_spider.spiders'
ITEM_PIPELINES  = {
    'wenkr_spider.pipelines.WenkrPipeline' : 100
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wenkr (+http://www.yourdomain.com)'
