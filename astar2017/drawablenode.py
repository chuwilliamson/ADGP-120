'''drawable nodes '''
import pygame


class DrawableNode(object):
    '''drawable node'''

    def __init__(self, graphnode):
        # astar vars
        posx = graphnode.value[0]
        posy = graphnode.value[1]
        self.adjacents = []
        self.parent = None
        self._walkable = True
        self._gscore = 0
        self._hscore = 0
        self._fscore = 0

        # drawing vars
        SIZE = 30
        self.width = SIZE
        self.height = SIZE
        self.id = id
        self.index = (posx, posy)
        self.value = self.index
        self.x = (5 + self.width) * posx + 5
        self.y = (5 + self.height) * posy + 5
        self.pos = (self.width * posx, self.height * posy)
        self.screenpos = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))
        self.dirty = False
        self._color = (125, 255, 255)

    # properties
    @property
    def walkable(self):
        '''is the node walkable'''
        return self._walkable

    @walkable.setter
    def walkable(self, value):
        '''block off a node'''
        self._walkable = value
        # if it's set to walkable change to white
        # this will mark it as undirty
        if value:
            self.color = (255, 255, 255)
        else:
            self.color = (255, 0, 0)

    @property
    def fscore(self):
        '''get fscore'''
        return self._fscore

    @property
    def gscore(self):
        '''get g cost'''
        return self._gscore

    @property
    def hscore(self):
        '''get h cost'''
        return self._hscore

    @fscore.setter
    def fscore(self, value):
        '''set f cost'''
        self._fscore = value

    @gscore.setter
    def gscore(self, value):
        '''set g cost'''
        self._gscore = value
        self._fscore = self._gscore + self._hscore

    @hscore.setter
    def hscore(self, value):
        '''set h score'''
        self._hscore = value
        self._fscore = self._gscore + self._hscore

    @property
    def color(self):
        '''get the color'''
        return self._color

    @color.setter
    # manual setting of colors will mark them dirty so they will stay
    def color(self, value):
        '''set color of node'''
        red = (255, 0, 0)

        if value is red:
            self._color = value
            self.dirty = True
        else:
            self._color = value

        self._color = value

    def info(self):
        '''get info of the node'''
        print("pos = ", self.pos)
        ids = ""
        for i in self.adjacents:
            ids += " " + str(i.id)
        print("neighbors:", ids)
        print("index: ", self.index)

    def draw(self, screen, font, init=True, text=False):
        '''draw a node'''
        self.surface.fill(self._color)
        screen.blit(self.surface, self.screenpos)
        if self.walkable:
            textf = font.render("F= " + str(self._fscore), True, (1, 1, 1))
            textg = font.render("G= " + str(self._gscore) +
                                "H= " + str(self._hscore), True, (1, 1, 1))

            # set it's position/parent
            textfpos = (self.x, self.y)  # top left
            textgpos = (self.x, self.y + self.height - 10)  # bot left

        # center it

        # draw the square
        if init and text:
            screen.blit(textf, textfpos)
            screen.blit(textg, textgpos)
