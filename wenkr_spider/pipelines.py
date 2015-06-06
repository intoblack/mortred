# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xsegment.summary import SimpleSummary
from doc import Doc
from wenkr_spider.spiders.config import get_doc_config
import re

class WenkrPipeline(object):
    summary = SimpleSummary()
    chinese = re.compile(ur'[\u4e00-\u9fa5a-z]{2,8}')

    '''
    创建pipeline
    '''

    def process_item(self, item, spider):
        item['summary'] = ''.join( [i.oristring for i in self.summary.summary(item['content'] , item['title'] , summary_sentences = 15)[1]])
        tags = [ tag for tag in item['tags'].split(',') if self.chinese.match(tag) and len(tag) < 8 ]
        item['tags'] = ','.join(tags)
        doc = Doc(item['title'] , item['content'] , item['author'] , item['category']  , item['tags'] ,item['summary'] )
        with open('%s/%s.md' % (get_doc_config()['content_path'] , item['title'] ), 'w') as f:
            f.write(str(doc))
        return item
