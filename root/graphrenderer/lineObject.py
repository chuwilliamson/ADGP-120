import root.graphrenderer.gameObject
import pygame
import root.graphrenderer.constants as constants


class LineObject:
    def __init__(self, value, edge):
        self.val = value
        self.edges = (edge[0], edge[1])
        self.color = constants.BLUE

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.edges[0]._pos, self.edges[1]._pos)
        