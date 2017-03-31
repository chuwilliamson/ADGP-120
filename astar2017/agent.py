'''agent.py'''
import math

import random

from gameobject import GameObject
from vector import Vector2

import pygame
import constants


class Agent(GameObject):
    '''agent'''

    def __init__(self, name, position, velocity):
        '''agent init'''
        super(Agent, self).__init__(name, position, 25, 25)
        self._target = Vector2(0, 0)
        self._force = Vector2(0, 0)
        self._velocity = velocity
        self._direction = self._velocity.normalized
        self._acceleration = Vector2(0, 0)
        self._mass = 1
        self._max_velocity = 50.0
        self.wanderangle = 45.0
        self._wanderforce = Vector2(0.0, 0.0)

    @property
    def position(self):
        '''position'''
        return Vector2(self._position.x, self._position.y - 800)

    @property
    def target(self):
        '''target'''
        return self._target

    def linear(self):
        '''linear force'''
        direction = self._velocity.normalized
        speed = self._velocity.magnitude
        return direction * speed

    @property
    def force(self):
        '''force with mass'''
        return self._force * (1 / self._mass)

    def add_force(self, force):
        '''add force to this gameobject'''
        self._force += force

    def update(self, deltatime):
        '''agent update'''
        self._force = self.seek() + self.wander(2, 4)
        self._acceleration = self.force
        self._velocity += self._acceleration * deltatime

        self._position += self._velocity * deltatime
        self._direction = self._velocity.normalized
        super(Agent, self).update(deltatime)

    def limit_velocity(self):
        '''limit velocity'''
        if self._velocity.magnitude > self._max_velocity:
            self._velocity = self._velocity * (1 / self._max_velocity)

    def _seek(self, target):
        '''seek to target'''
        displacement = target - self._position
        target_direction = displacement.normalized
        force = target_direction * self._max_velocity
        seekforce = force - self._velocity
        return seekforce

    def seek(self):
        '''seek'''
        return self._seek(self._target)

    def wander(self, distance, radius):
        '''wander force'''
        circlecenter = self._velocity.normalized
        circlecenter = circlecenter * distance

        displacement = self._velocity.normalized
        displacement = displacement * radius
        displacement.x = math.cos(self.wanderangle) * displacement.magnitude
        displacement.y = math.sin(self.wanderangle) * displacement.magnitude

        angle_change = 1.0
        self.wanderangle += random.random() * angle_change - angle_change * .5
        self._wanderforce = circlecenter + displacement
        return circlecenter + displacement

    def set_angle(self, vector, angle):
        '''set angle'''
        length = vector.magnitude
        vector.x = math.cos(angle) * length
        vector.y = math.sin(angle) * length

    def set_target(self, target):
        '''abc'''
        self._target = Vector2(target[0], target[1])

    def draw(self, screen):
        '''debug draw'''
        center = Vector2(self._position.x + self._width / 2,
                         self._position.y + self._height / 2)

        offset_dir = Vector2(center.x + self._direction.x * 25,
                             center.y + self._direction.y * 25)

        offset_upward = Vector2(center.x + self._up.x * 25,
                                center.y + self._up.y * 25)

        offset_forward = Vector2(center.x + self._forward.x * 25,
                                 center.y + self._forward.y * 25)

        pygame.draw.line(screen, constants.RED,
                         center.value, offset_dir.value, 2)
        pygame.draw.line(screen, constants.GREEN,
                         center.value, offset_upward.value, 2)
        pygame.draw.line(screen, constants.BLUE, center.value,
                         offset_forward.value, 2)

        offset_wander = Vector2(
            center.x + self._wanderforce.x * 10, center.y + self._wanderforce.y * 10)
        pygame.draw.line(screen, constants.BLACK,
                         center.value, offset_wander.value, 1)

        textpos = "Pos: <{0:.4} {1:.4}>".format(
            float(self._position.x), float(self._position.y))
        textdir = "Dir: <{0:.2} {1:.2}>".format(
            self._direction.x, self._direction.y)
        textwander = "Wander: <{0:.4} {1:.4}>".format(
            self._wanderforce.x, self._wanderforce.y)

        angle = math.atan2(self._direction.y,
                           self._direction.x) * 180 / (math.pi)
        if angle < 0:
            angle = 360 + angle
        textangle = "Angle: {0}".format(self.wanderangle)

        surface = self.font.render(textpos, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 50 + 0))

        surface = self.font.render(textdir, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 50 + 10))

        surface = self.font.render(textangle, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 50 + 20))

        surface = self.font.render(textwander, True, (0, 0, 0))
        screen.blit(surface, (self._position.x, self._position.y + 50 + 30))

        super(Agent, self).draw(screen)


if __name__ == '__main__':
    import main as Main
    Main.main()
