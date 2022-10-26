import math

from django.shortcuts import render
from .models import *
from .utils import get_coordinates

CENTER_TOP = 350
CENTER_LEFT = 500
RADIUS = 200
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
    size_invention_list = len(invention_list)
    alpha = ALPHAS_LIST[-1] // size_invention_list
    now_alpha = alpha

    radius = round(RADIUS * (1 + 0.1 * size_invention_list))

    for invention in invention_list:
        rad_alpha = math.radians(now_alpha)
        new_top = abs(round(math.sin(rad_alpha) * radius))
        new_left = abs(round(math.cos(rad_alpha) * radius))

        coordinates = get_coordinates(alpha=now_alpha, start_top=CENTER_TOP, start_left=CENTER_LEFT,
                                      new_top=new_top, new_left=new_left, radius=radius, delta=SIZE_DELTA)
        invention_result.append({
            'object': invention,
            'top': coordinates[1],
            'left': coordinates[0],
        })
        coordinates_list.append(list(x + CENTER_DELTA for x in coordinates))
        now_alpha += alpha

    context = {
        'scientist': scientist_result,
        'invention_list': invention_result,
        'coordinates_list': coordinates_list
    }
    return render(request, 'scientists_base/scientists_graph.html', context)
