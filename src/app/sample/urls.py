# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from rpc import Router

router = Router()

urlpatterns = patterns('sample.views',
    url(r'^$', 'index', name='index'),
    url(r'^router/$', router, name='router'),
    url(r'^router/api/$', router.api, name='api'),
)