# -*- coding: utf-8 -*-

from django import forms
from django.db.utils import IntegrityError

class CityForm(forms.Form):
    name = forms.CharField(required=True, max_length=40)
    
    def save(self,obj=None):
        from sample.models import City
        if not obj:
            obj = City()
        obj.name = self.cleaned_data['name']
        try:
            obj.save()
        except IntegrityError as error:
            return (False,obj,error[1].decode('utf8'))
        else:
            return (True,obj,'')

class StreetForm(forms.Form):
    city = forms.IntegerField(required=True)
    name = forms.CharField(required=True, max_length=40)

    def clean_city(self):
        from sample.models import City
        city = self.cleaned_data['city']
        try:
            city=City.objects.get(pk=city)
        except City.DoesNotExist:
            raise forms.ValidationError("City related object not exists.")
        return city

    def save(self,obj=None):
        from sample.models import Street
        if not obj:
            obj = Street()
        obj.city = self.cleaned_data['city']
        obj.name = self.cleaned_data['name']
        try:
            obj.save()
        except IntegrityError as error:
            return (False,obj,error[1].decode('utf8'))
        else:
            return (True,obj,'')

