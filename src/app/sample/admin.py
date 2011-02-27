# -*- coding: utf-8 -*-

from django.contrib import admin
from sample.models import *

"""
City
"""
class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)

"""
Street
"""
class StreetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Street, StreetAdmin)