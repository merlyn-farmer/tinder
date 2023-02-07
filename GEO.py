import numpy as np
import random
from shapely.geometry import Polygon, Point

def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)

    return points
# Choose the number of points desired. This example uses 20 points.

def geo_coords():
    poly = Polygon([(55.76664217677472, 37.536612561151145), (55.78421407372232, 37.551375439569114),
                    (55.78749585758228, 37.589827588006614), (55.77398085539273, 37.600813916131614),
                    (55.75640434392775, 37.585021069451926), (55.74442459958629, 37.57300477306521),
                    (55.74597057977355, 37.510863354608176)])

    points = polygon_random_points(poly, 1)
    for p in points:
        return p.x, p.y

latitude, longitude = geo_coords()
