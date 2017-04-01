'''predator.py'''

from agent import Agent
import pygame
import constants
from vector import Vector2


class Predator(Agent):
    '''PREDATOR'''

    def __init__(self, name, position, velocity, targets):
        '''agent init'''
        super(Predator, self).__init__(name, position, velocity)
        self.preys = targets
        self.goteem = False
        self.prey = self.preys[0]
        self._max_velocity = 10
        self._max_force = 20
        self.alive = 0
    def update(self, deltatime):
        '''update'''
        self.alive += deltatime
        self._force = Vector2(0, 0)
        for i in self.preys:
            curdist = self.position.distance(self.prey.position)
            chkdist = self.position.distance(i.position)
            if chkdist < curdist and self.prey != i:
                self.prey = i

        self._target = self.prey.position
        seekstr = self.position.distance(self._target)

        self.add_force(self.seek() * 10)
        if self.alive > 1:
            print self._force
            self.alive = 0
        super(Predator, self).update(deltatime)

    def draw(self, screen):
        '''draw'''
        super(Predator, self).draw(screen)


if __name__ == '__main__':
    import main as Main
    Main.main()
