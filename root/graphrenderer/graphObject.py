'''graphObject.py'''
import pygame
from pygame import *
from constants import *

class GraphObject:
    def __init__(self, value, position = [0,0]):
        self.val = value
        self.pos = position
        self.color = BLUE

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, self.pos, 20)
