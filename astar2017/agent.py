'''agent.py'''

from gameobject import GameObject
from vector import Vector2


class Agent(GameObject):
    '''agent'''

    def __init__(self, name, position, velocity):
        '''agent init'''
        super(Agent, self).__init__(name, position, 50, 50)
        self._target = Vector2(0, 0)
        self._force = Vector2(0, 0)
        self._velocity = velocity
        self._direction = self._velocity.normalized
        self._acceleration = Vector2(0, 0)
        self._mass = 1
        self._max_velocity = 20

    @property
    def position(self):
        '''position'''
        return self._position

    @property
    def target(self):
        '''target'''
        return self._target

    def linear(self):
        '''linear force'''
        direction = self._velocity.normalized
        speed = self._velocity.magnitude
        return direction * speed

    def add_force(self, force):
        '''add force to this gameobject'''
        self._force += force

    def update(self, deltatime):
        '''agent update'''

        self._acceleration = self._force + self.seek(self.target)
        self._velocity += self._acceleration * deltatime
        self._position += self._velocity * deltatime
        self._direction = self._velocity.normalized

    def seek(self, target):
        '''seek to target'''
        displacement = target - self._position
        target_direction = displacement.direction
        force = target_direction * self._max_velocity
        seekforce = force - self._velocity
        return seekforce

    def set_target(self, target):
        '''abc'''
        self._target = Vector2(target[0], target[1])
