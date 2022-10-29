from django.urls import path
from .views import *


urlpatterns = [
    # path('', index),
    path('search/', search, name='search'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('scientist/<int:scientist_id>/', scientist, name='scientist'),
    path('scientists_graph/<int:scientist_id>/', scientists_graph, name='scientists_graph'),
    path('inventions_graph/<int:invention_id>/', inventions_graph, name='inventions_graph'),
]

handler404 = 'scientists_base.views.page_not_found'
