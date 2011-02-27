# -*- coding: utf-8 -*-

from django.db.models.query import QuerySet
from django.db.models import Q
from django.utils.functional import update_wrapper
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder

def render_to(tpl=None):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter

    Parameters:

     - template: template name to use
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            if not tpl:
                template = '%s/%s.html' % (func.__module__.split('.')[1], func.__name__)
            else:
                template = tpl
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer

def render_to_json(func):
    def wrapper(request, *args, **kwargs):
        result = func(request, *args, **kwargs)
        json = simplejson.dumps(result, cls=DjangoJSONEncoder)
        return HttpResponse(json, mimetype="application/json")
    return wrapper

def store_read(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        rdata = args[1]
        if isinstance(result, tuple):
            result, success = result
        else:
            success = True
        if isinstance(result, QuerySet):
            total = result.count()
            print rdata
            if 'filter_fields' in rdata and 'filter_value' in rdata:
                if not rdata['filter_value']=='':
                    val = str(rdata['filter_value'])
                    query=None
                    for node in rdata['filter_fields']:
                        if query:
                            query = query | Q(**{"%s__icontains" % str(node):val})
                        else:
                            query = Q(**{"%s__icontains" % str(node):val})
                    if query:
                        result = result.filter(query)
            if 'start' in rdata and 'limit' in rdata:
                result = result[rdata['start']:rdata['start']+rdata['limit']]
            result = [obj.store_record() for obj in result]
        return dict(data=result, success=success, total=total)
    return update_wrapper(wrapper, func)