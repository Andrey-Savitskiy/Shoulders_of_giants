import math
from .models import *

CENTER_TOP = 500
CENTER_LEFT = 700
RADIUS = 200
FULL_ALPHA = 360

SIZE_DELTA = round((200 - 178) / 2)
SIZE_DELTA_THIRD = round((200 - 150) / 2)
CENTER_DELTA = round(178 / 2)


def get_coordinates(alpha: int, start_top: int, start_left: int,
                    new_top: int, new_left: int, radius: int, delta: int) -> tuple:
    start_top += delta
    start_left += delta

    if alpha < 90:
        return (start_left + new_left, start_top - new_top)
    elif alpha == 90:
        return (start_left, start_top - radius)
    elif 90 < alpha < 180:
        return (start_left - new_left, start_top - new_top)
    elif alpha == 180:
        return (start_left - radius, start_top)
    elif 180 < alpha < 270:
        return (start_left - new_left, start_top + new_top)
    elif alpha == 270:
        return (start_left, start_top + radius)
    elif 270 < alpha < 360:
        return (start_left + new_left, start_top + new_top)
    else:
        return (start_left + radius, start_top)


def get_first_object(first_object) -> dict:
    first_object_result = {
        'object': first_object,
        'top': CENTER_TOP,
        'left': CENTER_LEFT,
    }
    return first_object_result


def get_second_object_list(second_object_list):
    second_object_result = []
    coordinates_list = []
    size_second_object_list = len(second_object_list)
    alpha = FULL_ALPHA // size_second_object_list
    now_alpha = alpha

    radius = round(RADIUS * (1 + 0.1 * size_second_object_list))

    for second_object in second_object_list:
        rad_alpha = math.radians(now_alpha)
        new_top = abs(round(math.sin(rad_alpha) * radius))
        new_left = abs(round(math.cos(rad_alpha) * radius))

        coordinates = get_coordinates(alpha=now_alpha, start_top=CENTER_TOP, start_left=CENTER_LEFT,
                                      new_top=new_top, new_left=new_left, radius=radius, delta=SIZE_DELTA)
        second_object_result.append({
            'object': second_object,
            'top': coordinates[1],
            'left': coordinates[0],
        })
        coordinates_list.append(list(x + CENTER_DELTA for x in coordinates))
        now_alpha += alpha

    return second_object_result, coordinates_list


def get_third_object_list(third_object_list, second_object_result):
    third_object_result = {}
    coordinates_list = []

    size_third_object_list = len(third_object_list)
    alpha = FULL_ALPHA // size_third_object_list
    now_alpha = alpha
    radius = round(1.1 * RADIUS * (1 + 0.5 * size_third_object_list))

    for third_object in third_object_list:
        for second_object in second_object_result:
            result = Organization.objects.filter(pk=third_object.id).filter(scientist=second_object['object'])
            print(result)
            if result:
                if not third_object.id in third_object_result.keys():
                    print(alpha)

                    rad_alpha = math.radians(now_alpha)
                    new_top = abs(round(math.sin(rad_alpha) * radius))
                    new_left = abs(round(math.cos(rad_alpha) * radius))

                    coordinates = get_coordinates(alpha=now_alpha, start_top=CENTER_TOP, start_left=CENTER_LEFT,
                                                  new_top=new_top, new_left=new_left, radius=radius, delta=SIZE_DELTA_THIRD)

                    third_object_result[third_object.id] = {
                        'object': third_object,
                        'top': coordinates[1],
                        'left': coordinates[0],
                        'parents': [[second_object['top'], second_object['left']]],
                    }

                    coordinates_list.append([coordinates[1], coordinates[0], second_object['left'], second_object['top']])
                else:
                    print(alpha)
                    third_object_result[third_object.id]['parents'].append([second_object['top'], second_object['left']])
                    coordinates_list.append([third_object_result[third_object.id]['top'],
                                             third_object_result[third_object.id]['left'],
                                             second_object['left'], second_object['top']])
                now_alpha += alpha

    return list(third_object_result.values()), coordinates_list
