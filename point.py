import random


class Point:
    def __init__(self, radius):
        self.x = random.randint(-radius, +radius)

    def get_x(self):
        return self.x


def random_point(radius):
    return Point(radius)