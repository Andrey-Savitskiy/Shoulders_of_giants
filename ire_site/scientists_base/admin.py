from django.contrib import admin
from .models import *


# class ScientistInline(admin.TabularInline):
#     model = Scientist


class ScientistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'life_years']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
    # inlines = [ScientistInline]


# class OrganizationInline(admin.TabularInline):
#     model = Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
    # inlines = [OrganizationInline]


# class InventionInline(admin.TabularInline):
#     model = Invention


class InventionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['title', 'year']
    # inlines = [InventionInline]


class YearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']
    list_display_links = ['id', 'year']
    search_fields = ['year']
    list_filter = ['year']


admin.site.register(Scientist, ScientistAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Invention, InventionAdmin)
admin.site.register(Year, YearAdmin)
