"""
ADGP-120 Script it Up!
Matthew Williamson
"""
import math
import pygame
import random
from astar import *
from node import * 
import os



white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
teal = (128, 128, 255)
yellow = (255,255,0)

path = os.path.dirname(os.path.realpath(__file__))
def main():
	
	carImg = pygame.image.load(os.path.join(path ,'racecar.png'))
	
	#listen for click events
	mouse_listeners = []
	#create the search space to look through
	#dictionary b/c... I do not know how to declare a 2d array and i'm in the car
	search_space = {}
	id = 0
	ROWS = 15
	COLS = 15
	WIDTH = 60
	HEIGHT = 60
	for x in range(COLS):
		for y in range(ROWS):
		
			n = Node(x, y, id)
			#x goes right
			#y goes down
			if (x >= 5 and x <= 6 and y >= 5 and y <= 8):
				n.walkable = False
			
			leftWall = True if x % 15 == 0 else False
			rightWall = True if x % 15 == 15 - 1 else False
			topWall = True if y % 15 == 0 else False
			botWall = True if y % 15 == 15 - 1 else False
			
			if(leftWall or rightWall or topWall or botWall):
				n.walkable = False
			
			mouse_listeners.append(n.onclick)
			
			search_space[id] = n
			id+=1
		
	#create some random unwalkable terrain
	for i in range(20):
		rng = random.randint(0,(ROWS-1) * (COLS-1))			
		search_space[rng].walkable = False
			
	# Initialize pygame
	pygame.init()
	# Initialize fonts
	pygame.font.init()
	pad = (5,5)
	# Set the HEIGHT and WIDTH of the screen
	screen_width = COLS * (pad[0]  + WIDTH) + pad[1]
	screen_height = ROWS * (pad[0] + HEIGHT) + pad[1]
	# Set the screen
	screen = pygame.display.set_mode([screen_width, screen_height])
	font = pygame.font.Font(None, 14)
	# Set title of screen
	pygame.display.set_caption("ADGP-120 Astar")

	
	
	imgset = False
	Running = True
	algo = None
	start = None
	goal = None
	init = False
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(black)
	# -------- Main Program Loop -----------
	while Running:	
		#BEGIN INPUT HANDLING
		if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
			Running = False
		for event in pygame.event.get():  # User did something			
			if event.type == pygame.MOUSEBUTTONDOWN:#pressed mouse				
				for callback in mouse_listeners: #loop through all the subscribers
				#for click events
					cb = callback(pygame.mouse.get_pos())	
					if cb: #if the cb came back 
						if event.button == 1: #left click					
							print("left click")					
							for i in search_space:
								if not search_space[i].dirty:
									search_space[i].color = white #clear screen
							if(start):
								start._color = teal
							#screen.blit(carImg, start.pos)
							init = True
							if(start is None):
								print("must set start")
								init = False
								break

							else:
								print("goal set")
								
								cb.info()						
								goal = cb
								goal._color = yellow
								algo = Astar(search_space, start, goal)
								algo.Run()
								for i in algo.PATH:									
									if i is not start:
										i._color = green					
						if event.button == 3: #clear screen
							init = False
							if algo: algo.Reset()
							for i in search_space:
								if not search_space[i].dirty:
									search_space[i].color = white
									
							if not cb.dirty:
								print("set start")
								cb.info()
								start = cb
								start._color = teal
								imgset = True
								
								
			if event.type == pygame.QUIT:
				Running = False
		#END INPUT HANDLING		
		
		
		#blit the background
		#so we don't bleed our lines when we redraw
		
		screen.blit(background,(0,0))	
		
		for i in search_space:
			search_space[i].draw(screen, font, init)
		
		for n in search_space:
			i = search_space[n]
			if i.parent:		
				parentmid = (i.parent.rect.centerx , i.parent.rect.centery)
				selfmid = (i.rect.centerx, i.rect.centery)
				newrect = i.rect.inflate(1-(i.width/2),1-(i.height/2))
				pygame.draw.ellipse(screen, (100,25,255), newrect, 1)
				pygame.draw.aaline(screen, (100,25,255), selfmid, parentmid, 5)
		#if(imgset):
			#screen.blit(carImg, start.screenpos)		
		pygame.display.flip()
		
	pygame.quit() 
 
if __name__ == '__main__': main()

