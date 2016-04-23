"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import math
import pygame
import random
from astar import *
from node import * 

true = True
false = False
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
teal = (128, 128, 255)
yellow = (255,255,0)
#def mag(a):
	#return math.sqrt(a[0]^2 + a[1]^2)
	
def main():
	
	Red = (255,255,255)
	Green = (0,255,0)     
	Yellow = (255,255,0)	
	#print("mag of 255,255", mag((255,255)))
	#create the search space to look through
	mouse_listeners = []
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
			
			leftWall = true if x % 15 == 0 else false
			rightWall = true if x % 15 == 15 - 1 else false
			topWall = true if y % 15 == 0 else false
			botWall = true if y % 15 == 15 - 1 else false
			
			if(leftWall or rightWall or topWall or botWall):
				n.walkable = False
			
			mouse_listeners.append(n.onclick)
			
			search_space[id] = n
			id+=1
		
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
	font = pygame.font.Font(None, 15)
	# Set title of screen
	pygame.display.set_caption("Astar")

	
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	
	
	Running = True
	algo = None
	start = None
	goal = None
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(black)
	# -------- Main Program Loop -----------
	while Running:		
		
		for event in pygame.event.get():  # User did something			
			if event.type == pygame.MOUSEBUTTONDOWN:
				for callback in mouse_listeners:
					cb = callback(pygame.mouse.get_pos())	
					if cb is not None:
						if event.button == 1: #left click					
							print("left click")							
							if(start is None):
								print("must set start")
								break

							else:
								print("goal set")
								cb.info()						
								goal = cb
								goal._color = yellow
								algo = Astar(search_space, start, goal)
								algo.Run()
								for i in algo.PATH:
									pygame.time.wait(1)
									i._color = green					
						if event.button == 3: #clear screen
							if algo: algo.Reset()
							for i in search_space:
								if not search_space[i].dirty:
									search_space[i].color = white																
							if not cb.dirty:
								print("set start")
								cb.info()
								start = cb
								start._color = teal
								

				
			if event.type == pygame.QUIT:
				Running = False
		
		if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
			Running = False
		screen.blit(background,(0,0))
		for i in search_space:
			search_space[i].draw(screen, font)
		for n in search_space:
			i = search_space[n]
			if(i.parent):		
				parentmid = (i.parent.rect.centerx , i.parent.rect.centery)
				selfmid = (i.rect.centerx, i.rect.centery)
				pygame.draw.ellipse(screen, (100,25,255), selfmid, 5)
				pygame.draw.aaline(screen, (100,25,255), selfmid, parentmid, 5)
		pygame.display.flip()
		clock.tick(60)
			
		
		# Go ahead and update the screen with what we've drawn.
		
		

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	
	pygame.quit() 
 
if __name__ == '__main__': main()

