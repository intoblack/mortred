from django.template import Template , Context
from django.http import HttpResponse
from django.template.loader import get_template


import django

from django.conf import settings
# from django.core.management import setup_environ


def show_index(titles):
    t = get_template('index.html')
    html = t.render(Context({'titles' : [ 12 ,2 , 3]}))
    return HttpResponse(html)




if __name__ == '__main__':
    django.setup()
    # settings.configure()
    show_index([])










