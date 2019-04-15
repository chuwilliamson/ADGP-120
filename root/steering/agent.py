'''agent.py'''

from graphrenderer.graphObject import GraphObject

from math import sqrt

from utilities.vec2 import vec2

class Agent:
    def __init__(self, pos = vec2(), vel= vec2(), renderer= None):
        self.drawable = renderer
        self.position = pos
        self.velocity = vel
        
    
    def update(self, dt):   
        velocity = self.velocity     
        self.position += self.velocity        
        self.drawable.pos = [self.position[0], self.position[1]]

    def draw(self, screen):
        self.drawable.draw(screen)


    

def test(func, expected):
    return func[0](func[1][0], func[1][1]) == expected

def add(v1, v2):
    return v1 + v2

test(add, (vec2(0,0), vecw(1,1)), vec2(1,1))




