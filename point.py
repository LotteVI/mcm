import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


def random_point(radius):
    x = random.randint(-radius, +radius)
    y = random.randint(-radius, +radius)
    return Point(x, y)
