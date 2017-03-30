
'''vector helpers'''
import math


class Vector2(object):
    '''vector2 class'''

    def __init__(self, xpos, ypos):
        '''init'''
        self._value = (xpos, ypos)
        self._x = self._value[0]
        self._y = self._value[1]

    def _setx_(self, value):
        self._x = value
        self._value = (value, self._y)

    def _sety_(self, value):
        self._y = value
        self._value = (self._x, value)

    def _getx_(self):
        return self._x

    def _gety_(self):
        return self._y

    x = property(_getx_, _setx_)
    y = property(_gety_, _sety_)

    def __add__(self, other):
        '''add vector to vector'''
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''subtract vector from vector'''
        return Vector2(self.x - other.x, self.y - other.y)

    @property
    def value(self):
        '''return the value'''
        return (self.x, self.y)

    @property
    def magnitude(self):
        '''magnitude'''
        return self.get_magnitude()

    @property
    def normalized(self):
        '''aaa'''
        return self.get_direction()

    def __iadd__(self, other):
        '''+= operation'''
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def get_magnitude(self):
        '''assume a tuple as v1'''
        sqrmag = self.x * self.x + self.y * self.y
        return math.sqrt(sqrmag)

    def __getitem__(self, key):
        return self._value[key]

    def get_direction(self):
        '''get direction of vector'''
        v_mag = self.magnitude
        if v_mag == 0:
            return Vector2(0, 0)
        return Vector2(self.x * (1 / v_mag), self.y * (1 / v_mag))

    def displacement(self, vector2):
        '''get displacement between two vectors- straight line distance'''
        return Vector2(vector2.x - self.x, vector2.y - self.y)

    def dot(self, other):
        '''dot product'''
        return (self.x * other.x) + (self.y * other.y)

    def distance(self, vector2):
        '''get the distance of two vectors'''
        displacement = self.displacement(vector2)
        return math.fabs(displacement.magnitude)

    def __str__(self):
        '''get info'''
        res = "<{0}, {1}>".format(self.x, self.y)
        res.format(self.x, self.y)
        return res

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y


def test_add(a, b, result):
    '''test addition'''
    if a + b != result:
        print 'fail'
    else:
        print 'pass'
# tests
if __name__ == '__main__':
    a = Vector2(25, 25)
    b = Vector2(35, 35)
    c = Vector2(-35, -35)
    d = Vector2(35, 35)
    test_add(a, b, Vector2(60, 60))
    test_add(c, d, Vector2(0, 0))
