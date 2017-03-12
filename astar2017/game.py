'''game.py'''
from gameobject import GameObject
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(object):
    '''pygame object'''
    def __init__(self):
        '''abc'''
        self._name = ""        
        pygame.display.init()
        pygame.font.init()        
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()        
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()        
        self._background.fill(BLACK)
        self._gamestates = {}
        self._gamestates["init"] =  ["running"]
        self._gamestates["running"] =  ["pause", "quit"]
        self._gamestates["pause"] = ["running", "quit"]
        self._gamestates["quit"] = []
        self._currentstate = "init"
        self._events = pygame.event.get()
        
    
    def _set_state(self, value):        
        '''set state of the game'''
        if value in self._gamestates[self._currentstate]:
            print "newstate =>", self._currentstate, "to", value
            self._currentstate = value
        else:
            print "can not go from " , self._currentstate, "to", value

    def _get_state(self):
        return self._currentstate
    
    gamestate = property(_get_state, _set_state)

    def _startup(self):
        pygame.display.set_caption(self._name) 
        self._set_state("running")
        return True

    def _update(self):
        if self._get_state() == "quit":
            return False        
        self._clock.tick(10)
        self._events = pygame.event.get()
        for event in self._events:
            if event.type == pygame.constants.QUIT:
                self._set_state("quit")                       
            
            
        return True

    def _draw(self):       
        return 0 
                        

    def _shutdown(self):
        pygame.quit()

class LiamsGame(Game):    
    '''need documentation'''
    def __init__(self, name):
        '''need documentation'''
        super(LiamsGame, self).__init__()
        self._name = name
        self._gameobjects = []
        
        self._font = pygame.font.Font(None, 24)
        self.pause_surface = pygame.Surface((self._screen.get_size()[0]/3, self._screen.get_size()[1]/3))
        self.pause_surface.fill(GREEN)
        self.pause_rect = self.pause_surface.get_rect()
    
    def addtobatch(self, gameobject):
        '''need documentation'''
        self._gameobjects.append(gameobject)

    def update(self):
        if not super(LiamsGame, self)._update():
            return False
        for event in self._events:            
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()        
                if keystate[pygame.constants.K_e]:
                    self.gamestate = "pause"
                if keystate[pygame.constants.K_r]:
                    self.gamestate = "running"

        for go in self._gameobjects:
            go.update(self._events)
        

        return True

    def draw(self):
        '''need documentation'''            
        self._screen.blit(self._background, (0,0))
        for go in self._gameobjects:                        
            go.draw(self._screen)
            
        if(self.gamestate == "pause"):
            
            self.pause_surface.blit(self._font.render("PAUSED", True, WHITE), self.pause_rect.move(SCREEN_WIDTH/3,SCREEN_HEIGHT/3))
            
            self._screen.blit(self._background, (0,0))
            self._screen.blit(self.pause_surface, (0,0))
       
        pygame.display.flip()

        

    def run(self):
        '''need documentation'''
        if super(LiamsGame,self)._startup():
            while self.update():
                self.draw()                
        super(LiamsGame, self)._shutdown()

def main():
    game = LiamsGame("Liams game")
    player = GameObject("liam", (400, 300), 30, 30)
    game.addtobatch(player)
    game.run()

if __name__ == "__main__":
    main()