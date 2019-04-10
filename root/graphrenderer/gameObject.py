import math
import pygame
import root.graphrenderer.constants

class GameObject:
    def __init__(self, position = [0,0]):
        self.pos = position
        self.color = None

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):
        '''
        surface = pygame.Surface((30, 30))
        surface.fill(constants.BLACK)
        screen.blit(surface, self.pos)
        '''
