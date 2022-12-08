class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return str('(' + str(self.x) + ', ' + str(self.y) + ')')

    def __repr__(self):  # zwraca string "Point(x, y)"
        return str('Point(' + str(self.x) + ', ' + str(self.y) + ')')

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __sub__(self, other):  # v1 - v2
        self.x = self.x - other.x
        self.y = self.y - other.y
        return self

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return (self.x + self.y) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points
