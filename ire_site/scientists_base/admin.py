from django.contrib import admin
from .models import *


class ScientistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'life_years']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


class InventionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['title', 'year']


class YearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']
    list_display_links = ['id', 'year']
    search_fields = ['year']
    list_filter = ['year']


admin.site.register(Scientist, ScientistAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Invention, InventionAdmin)
admin.site.register(Year, YearAdmin)
