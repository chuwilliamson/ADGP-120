'''vec2.py'''

class vec2:
    def __init__(self, x = 0, y = 0):
        self.__value = [x, y]

    def __getitem__(self, key):
        return self.__value[key]

    def __add__(self, other):
        return vec2(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return vec2(self[0] - other[0], self[1] - other[1])

    def __iadd__ (self, other):        
        return self + other

    def __isub__(self, other):
        return self - other
    
    def __mult__(self, scalar):
        return vec2(self[0]*scalar, self[1] * scalar)

    def __str__(self):
        return str.format("x:%s, y:%s" % (self[0], self[1]))
    

