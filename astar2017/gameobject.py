'''gameobject to render'''

import math
import pygame.locals
import pygame.constants
from vector import Vector2
from constants import *


class GameObject(object):
    '''need documentation'''

    def __init__(self, name, position, width, height):
        '''make the go'''
        # Velocity += Force * deltaTime
        # Position += Velocity * deltaTime
        # Heading = normalise( Velocity )
        self._name = name
        self._width = width
        self._height = height
        self._color = WHITE
        self._surface = pygame.Surface(
            (self._width, self._height), pygame.SRCALPHA)

        points = [(0, 0), (0, height), (width, (height / 2))]

        self._position = Vector2(position[0], position[1])
        self._target = Vector2(0, 0)
        self._direction = Vector2(1, 0)
        self._forward = Vector2(1, 0)
        self._up = Vector2(0, 1)
        self.font = pygame.font.SysFont('mono', 12)

        pygame.draw.lines(self._surface, (125, 125, 255), True, points)
        pygame.transform.flip(self._surface, False, True)

    def draw(self, screen):
        '''draw the gameobject'''

        center = Vector2(self._position.x + self._width / 2,
                         self._position.y + self._height / 2)

        offset_dir = Vector2(center.x + self._direction.x * 25,
                             center.y + self._direction.y * 25)

        offset_upward = Vector2(center.x + self._up.x * 25,
                                center.y + self._up.y * 25)

        offset_forward = Vector2(center.x + self._forward.x * 25,
                                 center.y + self._forward.y * 25)

        pygame.draw.line(screen, RED, center.value, offset_dir.value, 2)
        pygame.draw.line(screen, GREEN, center.value, offset_upward.value, 2)
        pygame.draw.line(screen, BLUE, center.value, offset_forward.value, 2)
        pygame.draw.line(screen, BLACK, center.value, self._target.value, 1)
        textpos = "Pos: <{0:.4} {1:.4}>".format(
            self._position.x, self._position.y)
        textdir = "Dir: <{0:.2} {1:.2}>".format(
            self._direction.x, self._direction.y)
        dotp = self._forward.dot(self._direction)
        angle = math.atan2(self._position.y, self._position.x)
        textangle = "angle: {0}".format(dotp)

        surface = self.font.render(textpos, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 75))

        surface = self.font.render(textdir, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 75 + 15))

        surface = self.font.render(textangle, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 75 + 30))

        screen.blit(self._surface, (self._position.value))

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._position)
        return res
