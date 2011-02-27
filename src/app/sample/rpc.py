# -*- coding: utf-8 -*-

from extjs import RpcRouter
from decorators import store_read

class GridApiClass(object):

    def __init__(self,model,form):
        self.model = model
        self.form = form

    @store_read
    def read(self,rdata,request):
        return self.model.objects.all()
    read._args_len = 1

    def update(self,rdata,request):
        if not self.form:
            return dict(success=False, title="write error", msg="read only data", data={})
        result = []
        data = rdata['data']
        try:
            obj = self.model.objects.get(pk=data['id'])
        except self.model.DoesNotExist:
            return dict(success=False, msg="object not found")
        else:
            form = self.form(data)
            if form.is_valid():
                res = form.save(obj)
                ok = res[0]
                result.append(res[1].store_record())
                msg = res[2]
            else:
                ok = False
                msg = form._errors
        if ok:
            return dict(success=True, title="success", msg="saved", data=result)
        else:
            return dict(success=False, title="write error", msg=msg, data={})
    update._args_len = 1

    def create(self,rdata,request):
        if not self.form:
            return dict(success=False, title="write error", msg="read only data", data={})
        result = []
        data = rdata['data']
        form = self.form(data)
        if form.is_valid():
            res = form.save()
            ok = res[0]
            result.append(res[1].store_record())
            msg = res[2]
        else:
            ok = False
            msg = form._errors
        if ok:
            return dict(success=True, title="success", msg="saved", data=result)
        else:
            return dict(success=False, title="write error", msg=msg, data={})
    create._args_len = 1

    def destroy(self,rdata,request):
        print request.POST


class Router(RpcRouter):

    def __init__(self):
        from sample.models import City,Street
        from sample.forms import CityForm,StreetForm
        self.url = 'sample:router'
        self.actions = {
            'CityGrid': GridApiClass(City,CityForm),
            'StreetGrid': GridApiClass(Street,StreetForm),
        }
        self.enable_buffer = 50
