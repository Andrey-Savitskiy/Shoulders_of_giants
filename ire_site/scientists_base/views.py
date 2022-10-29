from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render

from .utils import *


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def about_us(request):
    context = {
        'header_name': 'О нас'
    }
    return render(request, 'scientists_base/about_us.html', context)


def contacts(request):
    context = {
        'header_name': 'Контакты'
    }
    return render(request, 'scientists_base/contacts.html', context)


def search(request):
    res = request.GET.get('q')
    search_vector = SearchVector("full_name", "short_name")
    search_query = SearchQuery(res)

    result = Organization.objects.annotate(
            search=search_vector, rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query)

    context = {
        'scientist_list': Scientist.objects.all(),
        'organization_list': Organization.objects.all(),
        'invention_list': Invention.objects.all(),
    }
    return render(request, 'scientists_base/search_results.html', context=context)


def scientist(request, scientist_id):
    scientist = Scientist.objects.get(id=scientist_id)
    invention_list = Invention.objects.filter(scientist=scientist)
    organization_list = Organization.objects.filter(scientist=scientist)

    context = {
        'scientist': scientist,
        'invention_list': invention_list,
        'organization_list': organization_list,
    }
    return render(request, 'scientists_base/scientist.html', context)


def scientists_graph(request, scientist_id):
    first_object = Scientist.objects.get(id=scientist_id)
    first_object_result = get_first_object(first_object)

    second_object = Invention.objects.filter(scientist=first_object)
    second_object_result, coordinates_list = get_second_object_list(second_object)

    context = {
        'first_object': first_object_result,
        'second_object_list': second_object_result,
        'coordinates_list': coordinates_list,
    }
    return render(request, 'scientists_base/scientists_graph.html', context)


def inventions_graph(request, invention_id):
    first_object = Invention.objects.get(id=invention_id)
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


