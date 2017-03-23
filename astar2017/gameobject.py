'''gameobject to render'''
# pylint: disable=E1121
import pygame.locals
import pygame.constants
import vector
from vector import *


class GameObject(object):
    '''need documentation'''

    def __init__(self, name, position, width, height):
        '''make the go'''
        # Velocity += Force * deltaTime
        # Position += Velocity * deltaTime
        # Heading = normalise( Velocity )
        self._name = name
        self._pos = position
        self._targetpos = Vector2(0, 0)
        self._force = Vector2(0, 0)
        self._velocity = Vector2(1, 0)
        self._direction = Vector2(1, 0)
        self._width = width
        self._height = height

        self._color = [255, 255, 255]
        self._surface = pygame.Surface((self._width, self._height))
        points = [(1, height - 1), (width, height - 1), ((width / 2), 0)]
        pygame.draw.lines(self._surface, (125, 125, 255), True, points)
        self._surface = self._surface.convert()

    def add_force(self, force):
        '''add force to this gameobject'''
        self._force = self._force

    def seek(self, target):
        '''seek to target'''
        max_velocity = 20
        displacement = get_displacement(self._pos, target)
        target_direction = get_direction(displacement)
        force = scale_vector(target_direction, max_velocity)
        seekforce = sub_vectors(force, self._velocity)

        return seekforce

    def update(self, deltatime):
        '''update gameobject logic'''
        self.add_force(scale_vector(self.seek(self._targetpos), 5))
        self._force = scale_vector(self._force, deltatime)
        self._velocity = add_vectors(
            self._velocity, scale_vector(self._force, deltatime))
        self._pos = add_vectors(self._pos, self._velocity)

    def draw(self, background):
        '''draw the gameobject'''

        center = (self._pos[0] + self._width / 2,
                  self._pos[1] + self._height / 2)
        color = (125, 125, 125)
        pygame.draw.line(background, color, center,
                         (center[0], center[1] - 30), 2)
        background.blit(self._surface, self._pos)

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._pos)
        return res
