'''gameobject to render'''
# pylint: disable=E1121
import pygame.locals
import pygame.constants
import Utilities.vector
from Utilities.vector import Vector2
import math


class GameObject(object):
    '''need documentation'''

    def __init__(self, name, position, width, height):
        '''make the go'''
        # Velocity += Force * deltaTime
        # Position += Velocity * deltaTime
        # Heading = normalise( Velocity )
        self._name = name
        self._position = Vector2(position[0], position[1])
        self._targetpos = Vector2(0, 0)
        self._force = Vector2(0, 0)
        self._velocity = Vector2(1, 0)
        self._direction = Vector2(1, 0)
        self._width = width
        self._height = height
        self._acceleration = Vector2(0, 0)
        self._mass = 1
        self._color = [255, 255, 255]
        self._surface = pygame.Surface(
            (self._width, self._height), pygame.SRCALPHA)

        points = [(0, 0), (0, height), (width, (height / 2))]
        pygame.draw.lines(self._surface, (125, 125, 255), True, points)
        # self._surface = self._surface.convert_alpha()

    def add_force(self, force):
        '''add force to this gameobject'''
        self._force = self._force + force

    def seek(self, target):
        '''seek to target'''
        max_velocity = 20
        displacement = target - self._position
        target_direction = displacement.direction
        force = target_direction * max_velocity
        seekforce = force - self._velocity
        return seekforce

    def set_target(self, target):
        '''abc'''
        self._targetpos = Vector2(target[0], target[1])

    def update(self, deltatime):
        '''update gameobject logic'''
        force = self.seek(self._targetpos)
        self.add_force(force * 5)
        self._force = self._force * deltatime
        self._acceleration = self._force * (1 / self._mass)
        self._velocity = self._velocity + self._force * deltatime
        self._direction = self._velocity.direction
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)

        self._position = self._position + self._velocity

    def draw(self, background):
        '''draw the gameobject'''

        center = (self._position.x + self._width / 2,
                  self._position.y + self._height / 2)
        offset = (center[0] + (self._direction.x * 25),
                  center[1] + (self._direction.y * 25))
        color = (125, 125, 125)
        pygame.draw.line(background, color, center, offset, 2)
        dotp = Vector2(1, 0).dot(self._direction)
        theta = math.acos(dotp)
        newsurface = pygame.transform.rotate(
            self._surface, theta * (180 / 3.14))

        background.blit(newsurface, (self._position.x, self._position.y))

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._position)
        return res
