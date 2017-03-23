'''vector helpers'''
import math


class Vector2(object):
    '''vector2 class'''

    def __init__(self, xpos, ypos):
        '''init'''
        self._value = (xpos, ypos)
        self._xpos = self._value[0]
        self._ypos = self._value[1]
        self.x = self._xpos
        self.y = self._ypos

    def __add__(self, other):
        '''add vector to vector'''
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''subtract vector from vector'''
        return Vector2(self.x - other.x, self.y - other.y)

    @property
    def magnitude(self):
        '''magnitude'''
        return self.get_magnitude()

    def get_magnitude(self):
        '''assume a tuple as v1'''
        sqrmag = self._xpos * self._xpos + self._ypos * self._ypos
        return math.sqrt(sqrmag)
    def __getitem__(self, key):
        return self._value[key]

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
        return Vector2(vector2.x - self.x, vector2.y - self.y)

    def distance(self, vector2):
        '''get the distance of two vectors'''
        displacement = self.displacement(vector2)
        return math.fabs(displacement.magnitude)


    def __str__(self):
        '''get info'''
        res = ""
        res += "<" + str(self._xpos) + ", " + str(self._ypos) + ">"
        return res
    def __mul__(self, other):
        return Vector2(self._xpos * other, self._ypos * other)


# tests
if __name__ == '__main__':
    testv = Vector2(25, 25)
    testa = Vector2(35, 35)
    print testa + testv
    print testa - testv

    print "mult", testa * 5
    print testv.magnitude  # 35.3 or root2 * 25
    print testv.direction  # .7, .7
    print testv.distance(testa)  # 0

    print testa.distance(testv)  # 0
