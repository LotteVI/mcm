import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def in_circle(self, radius):
        return pow(self.x, 2) + pow(self.y, 2) <= pow(radius, 2)


def random_point(radius):
    x = random.randint(-radius, +radius)
    y = random.randint(-radius, +radius)
    return Point(x, y)
