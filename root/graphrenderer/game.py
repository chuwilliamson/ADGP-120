'''game.py'''
import pygame
from pygame import *
from constants import *


class Game(object):
    '''pygame object'''

    def __init__(self, name):
        '''name: the name of your game'''
        self._name = name
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()

        self._background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT),
                                          pygame.SRCALPHA)
        self._background.fill((255, 255, 255))
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        self._events = pygame.event.get()
        self._gameobjects = []
        self._playtime = 0.0
        self._deltatime = 0.0
        self._fps = 30

    def add_gameobject(self, *args):
        '''add a gameobject to be rendered'''
        self._gameobjects.extend(args)

    def _startup(self):
        '''start the game'''
        pygame.display.set_caption(self._name)
        return True

    def _update(self):
        '''input and time'''
        seconds = self._clock.tick(self._fps)
        self._deltatime = seconds / 1000.0
        self._playtime += self._deltatime
        self._events = pygame.event.get()
        for e in self._events:
            if e.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_ESCAPE]:
                    return False
            if e.type == pygame.constants.QUIT:
                return False
        for go in self._gameobjects:
            go.update(self._deltatime)
        return True

    def _draw(self):
        '''need docstring'''
        self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
            self._clock.get_fps(), " " * 5, self._playtime))
        for go in self._gameobjects:
            go.draw(self._screen)
        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))

    def _shutdown(self):
        '''shutdown the game properly'''
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        surface = self.font.render(text, True, (0, 0, 0))
        self._screen.blit(surface, (25, 25))
