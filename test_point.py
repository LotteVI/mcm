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
