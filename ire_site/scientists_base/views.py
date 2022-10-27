from django.shortcuts import render

from .utils import *


def index(request):
    return render(request, 'scientists_base/index.html')


def about_us(request):
    return render(request, 'scientists_base/about_us.html')


def scientists_graph(request):
    first_object = Scientist.objects.first()
    first_object_result = get_first_object(first_object)

    second_object = Invention.objects.filter(scientist=first_object)
    second_object_result, coordinates_list = get_second_object_list(second_object)

    context = {
        'first_object': first_object_result,
        'second_object_list': second_object_result,
        'coordinates_list': coordinates_list,
    }
    return render(request, 'scientists_base/scientists_graph.html', context)


def inventions_graph(request):
    first_object = Invention.objects.first()
    first_object_result = get_first_object(first_object)

    second_object_list = Scientist.objects.filter(invention=first_object)
    second_object_result, first_coordinates_list = get_second_object_list(second_object_list)
    print(second_object_list)

    third_object_list = Organization.objects.filter(invention=first_object)
    third_object_result, second_coordinates_list = get_third_object_list(third_object_list, second_object_result)
    print(second_coordinates_list)

    context = {
        'first_object': first_object_result,
        'second_object_list': second_object_result,
        'first_coordinates_list': first_coordinates_list,
        'second_coordinates_list': second_coordinates_list,
        'third_object_result': third_object_result,
    }

    return render(request, 'scientists_base/inventions_graph.html', context)


