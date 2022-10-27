from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('scientists/', scientists_graph),
    path('inventions/', inventions_graph),
    path('about_us/', about_us),
]
