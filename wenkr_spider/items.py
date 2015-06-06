# -*- coding: utf-8 -*-



#生成doc日志工具
#

from scrapy import Item , Field



class WenkrItem(Item):


    content = Field()
    title = Field()
    author = Field()
    category = Field()
    tags = Field()
    summary = Field()
    head_date = Field()
