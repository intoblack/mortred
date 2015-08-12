#coding=utf-8




from lxml import etree
from scrapy.selector import Selector
from scrapy.http import TextResponse


def extract_href( html ):
    if isinstance(html , unicode):
        _xpath = etree.HTML(html)
    else:
        _xpath = html 
    for link in _xpath.xpath("//a[contains(@class, 'title') and contains(@class, 'info_flow_news_title')]"):
        yield link

def extract_href_selector( url , content):
    for link in Selector(text= content).xpath("//a[contains(@class, 'title') and contains(@class, 'info_flow_news_title')]/@href").extract():
        yield link  

def open_html(path):
    with open(path) as f:
        content = ''.join(f.readlines())
    return content



def test_extract_href_selector():
    with open('index.html') as f:
        content =  ''.join(f.readlines())
    for link in extract_href_selector( 'http://36kr.com', content):
        print link

def extract_html_detail(path):
    content = open_html(path)
    _x = Selector(text = content )
    title = _x.xpath("//h1[@class='single-post__title']/text()").extract()[0]
    body = '\n'.join( Selector(text = content).xpath("//section[@class='article']//*/text()").extract() )
    date = _x.xpath("//time[@class='timeago']/@title").extract()[0]
    print title,date

if __name__ == '__main__':
    test_extract_href_selector()
    extract_html_detail('./5036293.html')
