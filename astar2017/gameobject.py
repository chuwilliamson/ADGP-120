'''gameobject to render'''

import math
import pygame.locals
import pygame.constants
import pygame.surface 
from vector import Vector2
from constants import *



class GameObject(object):
    '''need documentation'''

    def __init__(self, name, position, width, height):
        '''make the go'''        
        self._name = name
        self._width = width
        self._height = height
        self._color = WHITE
        self._surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)

        points = [(0, 0), (0, height), (width, (height / 2))]
        
        self.screen_position = position
        self.screenpos = Vector2(position[0], position[1])
        self._target = Vector2(0, 0)
        self._direction = Vector2(1, 0)
        self._forward = Vector2(1, 0)
        self._up = Vector2(0, 1)
        self.font = pygame.font.SysFont('mono', 6)

        pygame.draw.lines(self._surface, (125, 125, 255), True, points)
        pygame.transform.flip(self._surface, False, True)

    def draw(self, screen):
        '''draw the gameobject'''
        angle = math.atan2(self._direction.y,
                           self._direction.x) * 180 / (math.pi)
        newsurface = pygame.transform.rotate(self._surface, -angle)
        screen.blit(newsurface, (self.screenpos.value))

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self.screenpos)
        return res
