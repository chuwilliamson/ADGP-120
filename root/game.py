"""
ADGP-120 Script it Up!
Matthew Williamson
"""
import math
import pygame
import random
import os
from astar import *
from node import * 
from pygame.locals import *


#center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'


#Color		#(R,G,B)
Black	=(0,0,0)
White	=(255,255,255)
Red		=(255,0,0)
Lime	=(0,255,0)
Blue	=(0,0,255)
Yellow	=(255,255,0)
Cyan 	=(0,255,255)
Magenta =(255,0,255)
Silver	=(192,192,192)
Gray	=(128,128,128)
Maroon	=(128,0,0)
Olive	=(128,128,0)
Green	=(0,128,0)
Purple	=(128,0,128)
Teal	=(0,128,128)
Navy	=(0,0,128)
Sky 	= (128, 128, 255)
Gold	=(255,215,0)
Orange	=(255,165,0)

path = os.path.dirname(os.path.realpath(__file__))
def main():
	#listen for click events
	mouse_listeners = []
	#create the search space to look through
	#dictionary b/c... I do not know how to declare a 2d array and i'm in the car
	search_space = {}
	id = 0
	ROWS = 20
	COLS = 30
	WIDTH = 30
	HEIGHT = 30
	for x in range(COLS):
		for y in range(ROWS):
		
			n = Node(x, y, id)
			#x goes right
			#y goes down
			if (x >= 5 and x <= 6 and y >= 5 and y <= 8):
				n.walkable = False
			
			leftWall = True if x % COLS == 0 else False
			rightWall = True if x % COLS == COLS - 1 else False
			topWall = True if y % ROWS == 0 else False
			botWall = True if y % ROWS == ROWS - 1 else False
			
			if(leftWall or rightWall or topWall or botWall):
				n.walkable = False
			
			mouse_listeners.append(n.onclick)
			
			search_space[id] = n
			id+=1
		
	#create some random unwalkable terrain
	for i in range(50):
		rng = random.randint(0,(ROWS-1) * (COLS-1))			
		search_space[rng].walkable = False
	
	# Initialize pygame
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()
	# Initialize fonts
	pygame.font.init()
	pygame.mixer.init()
	pad = (5,5)
	# Set the HEIGHT and WIDTH of the screen
	screen_width = COLS * (pad[0]  + WIDTH) + pad[1]
	screen_height = ROWS * (pad[0] + HEIGHT) + pad[1]
	# Set the screen
	
	screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
	font1 = pygame.font.Font(None, 14)
	font2 = pygame.font.Font(None, 55)
	# Set title of screen
	pygame.display.set_caption("ADGP-120 Astar")		
	
	imgset = False
	Running = True
	Paused = False
	algo = None
	start = None
	goal = None
	init = False
	gen = None
	delay = 50 #delay for the path finding
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(Black)
	#carImg = pygame.image.load(os.path.join(path ,'racecar.png'))
	fin = pygame.mixer.Sound(os.path.join(path,'audio\goteem.wav'))
	jump = pygame.mixer.Sound(os.path.join(path,'audio\jump2.wav'))
	
	audioclips = [fin,jump]
	
		
	
	# -------- Main Program Loop -----------
	def reset_color():
		for i in search_space:					
			if search_space[i].walkable:
				search_space[i].color = White
			else:
				search_space[i].color = Red
				
	while Running:	
		#BEGIN INPUT HANDLING
		events = pygame.event.get()
		for event in events :  # User did something			
			if event.type==VIDEORESIZE:
				screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)				
				pygame.display.flip()
			if event.type == pygame.MOUSEBUTTONDOWN:#pressed mouse				
				for callback in mouse_listeners: #loop through all the subscribers
				#for click events
					cb = callback(pygame.mouse.get_pos())	
					if cb: #if the cb came back 
						#MIDDLE MOUSE WHEEL
						if event.button == 4 and cb is not start:							
							cb.walkable = True
							
						if event.button == 5 and cb is not start:							
							cb.walkable = True
							
						#MIDDLE MOUSE CLICK
						if event.button == 2  and cb is not start:#set an unwalkable area							
							cb.walkable = False
							
						else:							
							#LEFT CLICK							
							if event.button == 1:
								#AND NOT PAUSED
								if(not Paused):
									reset_color()
									print("left click")												
									if start is None: #user left clicked and a start node wasn't set so break and prompt them
										print("must set start")
										init = False
										break
									else:
										init = True								
										goal = cb
										goal.info()
										#hardset color
										#make a new astar
										algo = Astar(search_space, start, goal,(ROWS,COLS))
										
										#run the algo
										gen = algo.Run()
										for i in audioclips: i.stop()
								else:
									cb.walkable = False
									
							#RIGHT CLICK
							elif event.button == 3: #clear screen
								reset_color()
								init = False
								if algo: 
									algo.Reset()
									gen = None
								if not cb.dirty:
									print("set start")
									cb.info()
									start = cb
									
									
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					Running = False
				if event.key == pygame.K_f:				
					Paused = not Paused
				if event.key == pygame.K_r:
					print(delay)
					delay += 1
				if event.key == pygame.K_q:
					delay -= 1
					
			if event.type == pygame.QUIT:
				Running = False
		#END INPUT HANDLING		
		
		
		#blit the background
		#so we don't bleed our lines when we redraw
		
		screen.blit(background,(0,0))	
		
		for i in search_space:
			search_space[i].draw(background, font1, init, text = False)
		
		for i in search_space:
			node = search_space[i]
			if node.parent:		
				parentmid = (node.parent.rect.centerx , node.parent.rect.centery)
				selfmid = (node.rect.centerx, node.rect.centery)
				newrect = node.rect.inflate((node.width/1.25) * -1,(node.height/1.25) * -1)
				pygame.draw.ellipse(screen, (100,25,255), newrect, 1)
				pygame.draw.aaline(screen, (100,25,255), selfmid, parentmid, 5)
		try:
			start._color = Cyan		
			goal.color = Gold
		except:
			print "start not set\r",
			
		if(not Paused):		
			if gen:
				try:
					current = gen.next()
					jump.set_volume(.1)
					jump.play()
					
					
					if(current is not start):
						current._color = Silver
						
				except StopIteration:
					for i in algo.PATH:								
						if i is not start:
							i._color = Lime
					
					print("finished")
					for i in audioclips: i.stop()
					fin.set_volume(.75)
					fin.play()
					
					gen = None
					start = goal
		else:
			screen.blit(font2.render("PAUSED", True, (255, 255, 25)), background.get_rect())
		
		pygame.display.flip()
	
	pygame.quit()
	exit()
if __name__ == '__main__': main()

