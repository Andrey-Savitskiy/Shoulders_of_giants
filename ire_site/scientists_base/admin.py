from django.contrib import admin
from .models import *


# class ScientistInline(admin.TabularInline):
#     model = Scientist


class ScientistAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['full_name']
    # inlines = [ScientistInline]


# class OrganizationInline(admin.TabularInline):
#     model = Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['full_name']
    # inlines = [OrganizationInline]


# class InventionInline(admin.TabularInline):
#     model = Invention


class InventionAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_title', 'year']
    list_display_links = ['id', 'full_title']
    search_fields = ['full_title']
    list_filter = ['full_title', 'year']
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
