def get_coordinates(alpha: int, start_top: int, start_left: int,
                    new_top: int, new_left: int, radius: int, delta: int) -> tuple:
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
