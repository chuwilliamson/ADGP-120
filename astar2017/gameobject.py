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
        self._surface = pygame.Surface((self._width, self._height))
        points = [(1, height - 1), (width, height - 1), ((width / 2), 0)]
        pygame.draw.lines(self._surface, (125, 125, 255), True, points)
        self._surface = self._surface.convert()

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
        self._position = self._position + self._velocity

    def draw(self, background):
        '''draw the gameobject'''

        center = (self._position.x + self._width / 2,
                  self._position.y + self._height / 2)
        color = (125, 125, 125)
        pygame.draw.line(background, color, center,
                         (center[0], center[1] - 30), 2)
        background.blit(self._surface, (self._position.x, self._position.y))

    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._position)
        return res
