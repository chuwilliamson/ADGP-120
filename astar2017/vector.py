'''vector helpers'''
import math


class Vector2(object):
    '''vector2 class'''

    def __init__(self, xpos, ypos):
        '''init'''
        self._value = (xpos, ypos)
        self._xpos = self._value[0]
        self._ypos = self._value[1]

    def __add__(self, other):
        '''add vector to vector'''
        return (self._xpos + other._xpos, self._ypos + other._ypos)

    def __sub__(self, other):
        '''subtract vector from vector'''
        return (self._value[0] - other._xpos, self._value[1] - other._ypos)

    @property
    def magnitude(self):
        '''magnitude'''
        return self.get_magnitude()

    def get_magnitude(self):
        '''assume a tuple as v1'''
        sqrmag = self._xpos * self._xpos + self._ypos * self._ypos
        return math.sqrt(sqrmag)

    @property
    def direction(self):
        '''aaa'''
        return self.get_direction()

    def get_direction(self):
        '''get direction of vector'''
        v_mag = self.magnitude
        return Vector2(self._xpos / v_mag, self._ypos / v_mag)

    def displacement(self, vector2):
        '''get displacement between two vectors- straight line distance'''
        return Vector2(vector2._xpos - self._xpos, vector2._ypos - self._ypos)

    def distance(self, vector2):
        '''get the distance of two vectors'''
        displacement = self.displacement(vector2)
        return math.fabs(displacement.magnitude)

    def scalarmult(self, scalar):
        '''scale vectors'''
        return Vector2(self._xpos * scalar, self._ypos * scalar)

    def __str__(self):
        '''get info'''
        res = ""
        res += "<" + str(self._xpos) + ", " + str(self._ypos) + ">"
        return res


# tests
if __name__ == '__main__':
    testv = Vector2(25, 25)
    testa = Vector2(35, 35)
    print testa + testv
    print testa - testv
    print testv.magnitude  # 35.3 or root2 * 25
    print testv.direction  # .7, .7
    print testv.distance(testa)  # 0

    print testa.distance(testv)  # 0
