'''agent.py'''

from graphrenderer.graphObject import GraphObject

from math import sqrt

from utilities.vec2 import vec2

class Agent:
    def __init__(self, pos = vec2(), vel= vec2(), renderer= None):
        self.drawable = renderer
        self.position = vec2(pos[0],pos[1])
        self.velocity = vec2(vel[0], vel[1])
        
    
    def update(self, dt):
        if self.position[0] > 800 or self.position[0] < 0:
            self.position= vec2(400, self.position[1])
        if self.position[1] > 800 or self.position[1] < 0:
            self.position = vec2(self.position[0], 400)
        self.position += self.velocity      
        self.drawable.pos = [self.position[0], self.position[1]]

    def draw(self, screen):
        self.drawable.draw(screen)    