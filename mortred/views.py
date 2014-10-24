#coding=utf-8
from django.template import Template , Context
from django.http import HttpResponse
from django.template.loader import get_template


import django

from django.conf import settings
# from django.core.management import setup_environ


class Article(object):

    def __init__(self):
        self.title = '标题'
        self.summary = '摘要'
        self.ori_url = 'http://www.baidu.com'


def show_index(titles):
    t = get_template('index.html')
    html = t.render(Context({'articles' : [Article()] }))
    return HttpResponse(html)














