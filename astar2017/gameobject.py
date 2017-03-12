'''gameobject to render'''
import pygame.locals
import pygame.constants
class GameObject(object):
    '''need documentation'''
    def __init__(self, name, pos, width, height):
        self._name = name
        self._pos = pos
        self._width = width
        self._height = height
        self._x = (5 + self._width) * pos[0] + 5
        self._y = (5 + self._height) * pos[1] + 5        
        self._surface = pygame.Surface((self._width, self._height))
        
        self._color = [255, 255, 255]
        self._surface.fill(self._color)

    def draw(self, screen):
        '''draw the gameobject'''      
        self._surface.fill(self._color)
        screen.blit(self._surface, self._pos)
    
    def update(self, events):
        for event in events:
            if event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_d:
                    self._pos = (self._pos[0] + 80, self._pos[1])
                if event.key == pygame.constants.K_w:
                    self._pos = (self._pos[0], self._pos[1] - 80)
                if event.key == pygame.constants.K_a:
                    self._pos = (self._pos[0] - 80, self._pos[1])
                if event.key == pygame.constants.K_s:
                    self._pos = (self._pos[0], self._pos[1] + 80)

            #     print "go right"
            # if keystate == pygame.K_s:
            #     self._pos[1] - 1
            # if keystate == pygame.K_w:
            #     self._pos[1] + 1
            # if keystate == pygame.K_a:
            #     self._pos[0] - 1
                
    
    def __str__(self):
        '''get info'''
        res = ""
        res += "Name:" + str(self._name) + "\nPosition: " + str(self._pos)
        return res