from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt1.x - self.pt2.x)

    @property
    def height(self):
        return abs(self.pt1.y - self.pt2.y)

    @property
    def top_left(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottom_left(self):
        return self.pt1

    @property
    def top_right(self):
        return self.pt2

    @property
    def bottom_right(self):
        return Point(self.pt2.x, self.pt1.y)

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return str('[' + str(self.pt1.__str__()) + ', ' + str(self.pt2.__str__()) + ']')

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle(' + str(self.pt1.x) + ', ' + str(self.pt1.y) + ', ' + str(self.pt2.x) + ', ' + str(self.pt2.y) + ')'

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

    def area(self):  # pole powierzchni
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1 + Point(x, y)
        self.pt2 + Point(x, y)
        return self

    @staticmethod
    def from_points(points):
        pt1 = points[0]
        pt2 = points[1]
        return Rectangle(pt1.x, pt1.y, pt2.x, pt2.y)
