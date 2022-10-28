from django.urls import path
from .views import *


urlpatterns = [
    # path('', index),
    path('scientists/', scientists_graph),
    path('inventions/', inventions_graph),
    path('about_us/', about_us),
    path('contacts/', contacts),
    path('scientist/<int:scientist_id>/', scientist),
]

handler404 = 'scientists_base.views.page_not_found'
