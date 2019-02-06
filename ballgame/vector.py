"""Vector class."""

from __future__ import annotations

from numbers import Number


class Vector:
    """Vector class with most operations implemented."""
    def __init__(self, x: Number, y: Number):
        if not all(isinstance(c, Number) for c in (x, y)):
            raise TypeError('x and y must be numbers.')
        self._value = [x, y]

    @property
    def x(self):
        """X coordinate (dimension 0)."""
        return self._value[0]

    @x.setter
    def x(self, value: Number):
        self._value[0] = value

    @property
    def y(self):
        """Y coordinate (dimension 1)."""
        return self._value[1]

    @y.setter
    def y(self, value: Number):
        self._value[1] = value

    def distance(self, other: Vector) -> Number:
        """Distance between two points."""
        return abs(other - self)

    def __abs__(self):
        return sum(x ** 2 for x in self._value) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (isinstance(other, Vector)
                and self.x == other.x and self.y == other.y)

    def __getitem__(self, indices):
        return self._value.__getitem__(indices)

    def __iter__(self):
        return iter(self._value)

    def __len__(self):
        return 2

    def __mul__(self, other):
        try:
            return self.x * other.x + self.y * other.y
        except AttributeError:
            return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __round__(self, ndigits=None):
        return Vector(round(self.x, ndigits), round(self.y, ndigits))

    def __repr__(self):
        return f'Vector({", ".join(str(x) for x in self._value)})'

    def __str__(self):
        return repr(self)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
