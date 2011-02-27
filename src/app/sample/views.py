# -*- coding: utf-8 -*-

from decorators import render_to

@render_to('sample/index.html')
def index(request):
    return {}