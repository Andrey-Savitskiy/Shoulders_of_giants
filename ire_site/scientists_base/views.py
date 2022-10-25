import json
import math

from django.core import serializers
from django.shortcuts import render
from .models import *
from .utils import get_coordinates

CENTER_TOP = 350
CENTER_LEFT = 500
RADIUS = round(200 * 1.5)
ALPHAS_LIST = (90, 180, 270, 360)

SIZE_DELTA = round((200 - 178) / 2)
CENTER_DELTA = round(178 / 2)


def index(request):
    return render(request, 'scientists_base/index.html')


def scientists_graph(request):
    scientist = Scientist.objects.first()
    scientist_result = {
        'object': scientist,
        'top': CENTER_TOP,
        'left': CENTER_LEFT,
    }

    invention_list = Invention.objects.filter(scientist=scientist)
    invention_result = []
    coordinates_list = []
    alpha = ALPHAS_LIST[-1] // len(invention_list)
    now_alpha = alpha

    for invention in invention_list:
        new_top = round(math.sin(math.radians(now_alpha))  * RADIUS)
        new_left = round(math.cos(math.radians(now_alpha)) * RADIUS)
        print(math.radians(now_alpha))

        coordinates = get_coordinates(alpha=now_alpha, start_top=CENTER_TOP, start_left=CENTER_LEFT,
                                      new_top=new_top, new_left=new_left, radius=RADIUS, delta=SIZE_DELTA)
        invention_result.append({
            'object': invention,
            'top': coordinates[1],
            'left': coordinates[0],
        })
        coordinates_list.append(list(x + CENTER_DELTA for x in coordinates))
        print(now_alpha)
        print(invention.full_title)
        print(coordinates)
        print()
        now_alpha += alpha

    context = {
        'scientist': scientist_result,
        'invention_list': invention_result,
        'coordinates_list': coordinates_list
    }
    return render(request, 'scientists_base/scientists_graph.html', context)
