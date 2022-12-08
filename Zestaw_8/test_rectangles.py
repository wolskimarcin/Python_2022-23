import pytest
from points import Point
from rectangles import Rectangle


@pytest.fixture
def rect():
    rect = Rectangle(1, 2, 3, 4)
    return rect


def test_top(rect):
    assert rect.top == 4


def test_left(rect):
    assert rect.left == 1


def test_bottom(rect):
    assert rect.bottom == 2


def test_right(rect):
    assert rect.right == 3


def test_width(rect):
    assert rect.width == 2


def test_height(rect):
    assert rect.height == 2


def test_top_left(rect):
    assert rect.top_left == Point(1, 4)


def test_bottom_left(rect):
    assert rect.bottom_left == Point(1, 2)


def test_top_right(rect):
    assert rect.top_right == Point(3, 4)


def test_bottom_right(rect):
    assert rect.bottom_right == Point(3, 2)


def test_str(rect):
    assert str(rect) == "[(1, 2), (3, 4)]"


def test_repr(rect):
    assert repr(rect) == "Rectangle(1, 2, 3, 4)"


def test_eq(rect):
    rect2 = Rectangle(1, 2, 3, 4)
    assert rect == rect2


def test_ne(rect):
    rect2 = Rectangle(2, 3, 4, 5)
    assert rect != rect2


def test_center(rect):
    assert rect.center() == Point(2, 3)


def test_area(rect):
    assert rect.area() == 4


def test_move(rect):
    rect.move(2, 3)
    assert rect == Rectangle(3, 5, 5, 7)


def test_from_points(rect):
    pt1 = Point(1, 2)
    pt2 = Point(3, 4)
    assert Rectangle.from_points([pt1, pt2]) == Rectangle(1, 2, 3, 4)


if __name__ == "__main__":
    pytest.main()
