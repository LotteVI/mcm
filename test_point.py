import pytest
import point


@pytest.fixture
def radius():
    return 1000


@pytest.fixture
def random_point(radius):
    return point.random_point(radius)


def test_random_point_x(random_point, radius):
    assert abs(random_point.get_x()) <= radius


def test_random_point_y(random_point, radius):
    assert abs(random_point.get_y()) <= radius

test_point_in_circle_data = [
    (0, 0, True),
    (500, 500, True),
    (-500, 500, True),
    (-500, -500, True),
    (500, -500, True),
    (1000, 0, True),
    (0, 1000, True),
    (-1000, 0, True),
    (0, -1000, True),
    (1000, 1000, False),
    (-1000, 1000, False),
    (-1000, -1000, False),
    (1000, -1000, False),
    (707, 707, True),
    (707, 708, False),
    (708, 707, False),
    ]
@pytest.mark.parametrize("x, y, result", test_point_in_circle_data)
def test_point_in_circle(x, y, result):
    assert point.Point(x, y).in_circle(1000) == result
