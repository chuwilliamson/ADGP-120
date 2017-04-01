'''agent.py'''
import math

import random

from gameobject import GameObject
from vector import Vector2

import pygame
import constants


def set_angle(vector, angle):
    '''set angle'''
    length = vector.magnitude
    vector.x = math.cos(angle) * length
    vector.y = math.sin(angle) * length


def limit_velocity(vector, maxv):
    '''limit velocity'''
    length = maxv / vector.magnitude
    vector = vector * length


class Agent(GameObject):
    '''agent'''

    def __init__(self, name, position, velocity):
        '''agent init'''
        self.size = 50
        super(Agent, self).__init__(name, position, self.size, self.size)
        self._target = Vector2(0, 0)
        self._force = Vector2(0, 0)
        self._velocity = velocity
        self._direction = self._velocity.normalized
        self._acceleration = Vector2(0, 0)
        self._mass = 1
        self._max_velocity = 10
        self._max_force = 10
        self._wanderangle = math.pi / 4

    @property
    def position(self):
        '''position'''
        return Vector2(self._position.x, self._position.y)

    @property
    def target(self):
        '''target'''
        return self._target

    @property
    def targetpos(self):
        '''target'''
        return self._target

    @property
    def force(self):
        '''force with mass'''
        return self._force * (1 / self._mass)

    def add_force(self, force):
        '''add force to this gameobject'''
        if force.magnitude > self._max_force:
            force = force.normalized * self._max_force
        self._force += force

    def update(self, deltatime):
        '''agent update'''
        self._acceleration = self.force
        self._velocity += self._acceleration * deltatime
        limit_velocity(self._velocity, self._max_velocity)
        self._position += self._velocity * deltatime
        self._direction = self._velocity.normalized
        super(Agent, self).update(deltatime)

    def _seek(self, target):
        '''seek to target'''
        displacement = target - self._position
        force = displacement.normalized * self._max_velocity
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
        set_angle(displacement, self._wanderangle)

        angle_change = .5
        self._wanderangle += random.random() * angle_change - angle_change * .5
        self._wanderforce = circlecenter + displacement
        return circlecenter + displacement

    def set_target(self, target):
        '''abc'''
        self._target = Vector2(target[0], target[1])

    def draw_forces(self, screen):
        '''debug draw'''
        pos = self._position
        direction = self._direction
        width = self._width
        height = self._height
        velocity = self._velocity

        center = Vector2(pos.x + width / 2, pos.y + height / 2)

        offset_dir = center + self._velocity * self.size

        offset_seek = Vector2(center.x + self._seekforce.x *
                              10, center.y + self._seekforce.y * 10)
        offset_wander = Vector2(
            center.x + self._wanderforce.x * 10, center.y + self._wanderforce.y * 10)

        angle = math.atan2(direction.y, direction.x)
        angle = angle * 180 / (math.pi)
        if angle < 0:
            angle = 360 + angle

        textpos = "Pos: <{0:.4} {1:.4}>".format(float(pos.x), float(pos.y))
        textdir = "Dir: <{0:.2} {1:.2}>".format(direction.x, direction.y)
        textvelocity = "Velocity: <{0:.4} {1:.4}>".format(
            float(velocity.x), float(velocity.y))

        textangle = "Angle: {0}".format(self._wanderangle)

        pygame.draw.line(screen, constants.BLACK,
                         center.value, offset_wander.value, 1)

        pygame.draw.line(screen, constants.BLACK,
                         center.value, offset_seek.value, 1)

        pygame.draw.line(screen, constants.RED,
                         center.value, offset_dir.value, 2)

        #pygame.draw.circle(screen, constants.RED, self._target.value, 25)

        surface = self.font.render(textpos, True, (0, 0, 0))
        screen.blit(surface, (pos.x, pos.y + self.size * 2 + 0))

        surface = self.font.render(textdir, True, (0, 0, 0))
        screen.blit(surface, (pos.x, pos.y + self.size * 2 + 10))

        surface = self.font.render(textangle, True, (0, 0, 0))
        screen.blit(surface, (pos.x, pos.y + self.size * 2 + 20))

        surface = self.font.render(textvelocity, True, (0, 0, 0))
        screen.blit(surface, (pos.x, pos.y + self.size * 2 + 30))

    def draw(self, screen):
        '''debug draw'''
        if constants.DEBUG:
            self.draw_forces(screen)
        super(Agent, self).draw(screen)

if __name__ == '__main__':
    import main as Main
    Main.main()
