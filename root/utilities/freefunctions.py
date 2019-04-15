'''freefunctions.py'''

from math import sqrt
def addvector(v1, v2):
    return 
def get_sqrmagnitude(vector):        
    return sum(list(map(lambda x : x * x, vector)))

def get_magnitude(vector):
    return sqrt(get_sqrmagnitude(vector))

def run(game):
    #add the gameObjects here
    if game._startup():#if the game starts up correctly
        while game._update():#update the game if the game updates then
            game._draw()#draw elements from the game
        game._shutdown()
