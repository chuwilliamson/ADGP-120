import root.graphrenderer.gameObject
import pygame
import root.graphrenderer.constants as constants


class GraphObject:
    def __init__(self, value, position = [0,0]):
        self.val = value
        self.pos = position
        self.color = constants.BLUE

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, self.pos, 20)
