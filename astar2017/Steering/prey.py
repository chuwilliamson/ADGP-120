'''prey.py'''


from agent import Agent
from vector import Vector2

import pygame


class Prey(Agent):
    '''PREY'''

    def __init__(self, name, position, velocity):
        '''agent init'''
        super(Prey, self).__init__(name, position, velocity)
        self._max_velocity = 18.0
        self._predator = None
        self.scared = False

    def update(self, deltatime):
        '''update'''
        self._force = Vector2(0, 0)
        self._target = self._predator.position
        if self._position.distance(self._predator.position) < 250:
            self.scared = True
        else:
            self.scared = False
        if self.scared:
            self.add_force(self.seek() * -1.0)

        self.add_force(self.wander(2, 1) * 10.0)
        super(Prey, self).update(deltatime)

    def set_target(self, target):
        self._predator = target

    def draw(self, screen):
        '''draw'''

        super(Prey, self).draw(screen)

if __name__ == '__main__':
    import main as Main
    Main.main()
