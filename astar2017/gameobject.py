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
        self._surface = pygame.Surface(
            (self._width, self._height), pygame.SRCALPHA)
        points = [(0, 0), (0, height), (width, (height / 2)), (0, 0)]
        self._position = Vector2(position[0], position[1])
        self._target = Vector2(0, 0)
        self._direction = Vector2(1, 0)
        self._forward = Vector2(1, 0)
        self._up = Vector2(0, 1)
        self.font = pygame.font.SysFont('mono', 10)
        self.image = pygame.image.load('racecar.png')
        pygame.draw.lines(self._surface, (125, 125, 255), False, points)

    def draw(self, screen):
        '''draw the gameobject'''
        angle = math.atan2(self._direction.y,
                           self._direction.x) * 180 / (math.pi)
        if angle < 0:
            angle = 360 + angle
        newsurface = pygame.transform.rotate(self._surface, -angle)
        screen.blit(newsurface, (self._position.value))

    def update(self, deltatime):
        '''update this go'''
        center = Vector2(SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2)
        if self._position.distance(center) > 400 + deltatime:
            self._position = center

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._position)
        return res



if __name__ == '__main__':
    import main as Main
    Main.main()
