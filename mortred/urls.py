from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'mortred.views.show_index'),
    url(r'^admin/', include(admin.site.urls)),
)
