'''gameobject to render'''

import math
import pygame.locals
import pygame.constants
import pygame.surface
from vector import Vector2
import constants
import random


class GameObject(object):
    '''need documentation'''

    def __init__(self, name, position, width, height):
        '''make the go'''
        self._name = name
        self._width = width
        self._height = height
        self._color = constants.WHITE
        self._surface = pygame.Surface(
            (self._width, self._height), pygame.SRCALPHA)
        points = [(0, 0), (0, height), (width, (height / 2)), (0, 0)]
        self._position = Vector2(position[0], position[1])
        self._target = Vector2(0, 0)
        self._direction = Vector2(1, 0)
        self._forward = Vector2(1, 0)
        self._up = Vector2(0, 1)
        self.font = pygame.font.SysFont('mono', 10)
        image = pygame.image.load('Steering/' + name + '.png')
        self.runningtime = 0
        self.image = pygame.transform.rotate(image, 270)

        pygame.draw.lines(self._surface, (125, 125, 255), False, points)

    def draw(self, screen):
        '''draw the gameobject'''
        angle = math.atan2(self._direction.y,
                           self._direction.x) * 180 / (math.pi)
        if constants.DEBUG:
            self._surface = pygame.Surface((self._width, self._height))
        else:
            self._surface = pygame.Surface(
                (self._width, self._height), pygame.SRCALPHA)
        # offset_upward = Vector2(center.x + self._up.x * self.size,
        #                         center.y + self._up.y * self.size)

        # offset_forward = Vector2(center.x + self._forward.x * self.size,
        #                          center.y + self._forward.y * self.size)

        if angle < 0:
            angle = 360 + angle
        image = pygame.transform.rotate(self.image, -angle)
        screen.blit(image, (self._position.value))

        newsurface = pygame.transform.rotate(self._surface, -angle)
        screen.blit(newsurface, (self._position.value))

    def update(self, deltatime):
        '''update this go'''
        if self._position.x > constants.SCREEN_WIDTH or self._position.x < 0:
            self._position = Vector2(
                constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
        if self._position.y > constants.SCREEN_HEIGHT or self._position.y < 0:
            self._position = Vector2(
                constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

        self.runningtime += deltatime

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._position)
        return res


if __name__ == '__main__':
    import main as Main
    Main.main()
