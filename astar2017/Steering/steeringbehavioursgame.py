'''concrete game'''
import pygame
import constants
from game import Game


class SteeringBehavioursGame(Game):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(SteeringBehavioursGame, self).__init__()
        self._name = name
        self._gameobjects = []

    def addtobatch(self, gameobject):
        '''need documentation'''
        self._gameobjects.append(gameobject)

    def update(self):
        '''need documentation'''
        if not super(SteeringBehavioursGame, self)._update():
            return False
        for event in self._events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_s]:
                    pass
                if keystate[pygame.constants.K_d]:
                    constants.DEBUG = not constants.DEBUG
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        for i in self._gameobjects:
            i.update(self._deltatime)

        return True

    def draw(self):
        '''need documentation'''
        for i in self._gameobjects:
            i.draw(self._screen)
        super(SteeringBehavioursGame, self)._draw()

    def run(self):
        '''need documentation'''
        if super(SteeringBehavioursGame, self)._startup():
            while self.update():
                self.draw()
        super(SteeringBehavioursGame, self)._shutdown()

if __name__ == '__main__':
    import main as Main
    Main.main()
