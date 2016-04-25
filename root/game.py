"""
ADGP-120 Script it Up!
Matthew Williamson
"""

import math
import pygame
import random
import os
import astar
import node
import pygame.locals
from astar import *
from node import * 
from pygame import mixer
from pygame.locals import *
'''
from os import *
from math import *
from random import *
from pygame import *
'''
	#Color		#(R,G,B)
Black	=(55,55,155)
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

class Game:
	def __init__(self):
		#center the window
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		path = os.path.dirname(os.path.realpath("__file__"))
		pygame.init()
		# Initialize fonts
		pygame.font.init()
		pygame.mixer.pre_init(44100, -16, 1, 512)
		pygame.mixer.init()
		#create the search space to look through
			#dictionary b/c... I do not know how to declare a 2d array and i'm in the car
		
		self.search_space = {}
		#listen for click events
		self.mouse_listeners = []
		
		id = 0
		self.ROWS = 20
		self.COLS = 50
		self.WIDTH = 30
		self.HEIGHT = 30
		for x in range(self.COLS):
			for y in range(self.ROWS):
				
				n = Node(x, y, id)
				#x goes right
				#y goes down
				if (x >= 5 and x <= 6 and y >= 5 and y <= 8):
					n.walkable = False
				
				leftWall = True if x % self.COLS == 0 else False
				rightWall = True if x % self.COLS == self.COLS - 1 else False
				topWall = True if y % self.ROWS == 0 else False
				botWall = True if y % self.ROWS == self.ROWS - 1 else False
				
				if(leftWall or rightWall or topWall or botWall):
					n.walkable = False
				
				self.mouse_listeners.append(n.onclick)
				
				self.search_space[id] = n
				id+=1
			
		#create some random unwalkable terrain
		mod = 15
		for i in range(50 + 50 + 50):
			rng = random.randint(0,(self.ROWS-1) * (self.COLS-1))			
			self.search_space[rng].walkable = False
		
		# Initialize pygame
		
		
		pad = (5,5)
		# Set the HEIGHT and WIDTH of the screen
		screen_width = self.COLS * (pad[0]  + self.WIDTH) + pad[1]
		screen_height = self.ROWS * (pad[0] + self.HEIGHT) + pad[1]
		# Set the screen
		
		self.screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
		
		self.font1 = pygame.font.Font(None, 14)
		self.font2 = pygame.font.Font(None, 28)
		# Set title of screen
		pygame.display.set_caption("ADGP-120 Astar")		
		
		self.imgset = False
		self.Running = True
		self.Paused = False
		self.algo = None
		self.start = None
		self.goal = None
		self.init = False
		self.gen = None
		self.delay = 50 #delay for the path finding
		
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(Black)
		#carImg = pygame.image.load(os.path.join(path ,'racecar.png'))
		self.fin = pygame.mixer.Sound(os.path.join(path,'audio\goteem.wav'))
		self.jump = pygame.mixer.Sound(os.path.join(path,'audio\jump1.wav'))
		
		self.audioclips = [self.fin,self.jump]
	
	def reset_color(self):
		for i in self.search_space:					
			if self.search_space[i].walkable:
				self.search_space[i].color = White
			else:
				self.search_space[i].color = Red	
			
		
		# -------- Main Program Loop -----------

	def run(self):
		debug = False
		while self.Running:	
			#BEGIN INPUT HANDLING
			events = pygame.event.get()
			for event in events :  # User did something			
				if event.type==VIDEORESIZE:
					self.screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)				
					pygame.display.flip()
				if event.type == pygame.MOUSEBUTTONDOWN:#pressed mouse				
					for callback in self.mouse_listeners: #loop through all the subscribers
					#for click events
						cb = callback(pygame.mouse.get_pos())	
						if cb: #if the cb came back 						
							if cb:		
								#LEFT CLICK							
								if event.button == 1:
									#AND NOT PAUSED
									if(not self.Paused):
										self.reset_color()
										print("left click")												
										if self.start is None: #user left clicked and a start node wasn't set so break and prompt them
											print("must set start")
											self.init = False
											break
										else:
											self.init = True								
											self.goal = cb
											self.goal.info()
											#hardset color
											#make a new astar
											self.algo = Astar(self.search_space, self.start, self.goal,(self.ROWS,self.COLS))
											
											#run the algo
											self.gen = self.algo.Run()
											for i in self.audioclips: i.stop()
									else:
										if cb is not self.start or cb is not self.goal:
											cb.walkable = not cb.walkable
										
								#RIGHT CLICK
								elif event.button == 3: #clear screen
									self.reset_color()
									init = False
									if self.algo: 
										self.algo.Reset()
										self.gen = None
									if not cb.dirty:
										print("set start")
										cb.info()
										self.start = cb
										
										
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.Running = False						
					if event.key == pygame.K_f:				
						self.Paused = not self.Paused
						if self.Paused:
							pygame.mixer.pause()					
						if not self.Paused: 
							pygame.mixer.unpause()
					if event.key  == pygame.K_q:
						print self.delay,
					if event.key == pygame.K_r:
						print delay,
						self.delay += 15
					if event.key == pygame.K_q:
						self.delay -= 15					
					if event.key == pygame.K_d:
						debug = not debug
				if event.type == pygame.QUIT:
					self.Running = False
			#END INPUT HANDLING		
			
			
			#blit the background
			#so we don't bleed our lines when we redraw
	
			self.screen.blit(self.background,(0,0))	
			
			for i in self.search_space:
				self.search_space[i].draw(self.background, self.font1, self.init, debug)
			
			for i in self.search_space:
				node = self.search_space[i]
				if node.parent:		
					parentmid = (node.parent.rect.centerx , node.parent.rect.centery)
					selfmid = (node.rect.centerx, node.rect.centery)
					newrect = node.rect.inflate((node.width/1.25) * -1,(node.height/1.25) * -1)
					pygame.draw.ellipse(self.screen, (100,25,255), newrect, 1)
					pygame.draw.aaline(self.screen, (100,25,255), selfmid, parentmid, 5)
			try:
				self.start._color = Green
				self.goal.color = Gold
			except:
				print "start not set\r",
			
			bg = pygame.Surface((self.screen.get_size()[0]/3, self.screen.get_size()[1]/3))
			bg.fill(Gray)
			textrect = bg.get_rect()
				
			if(not self.Paused):		
				if self.gen:
					try:
						self.current = self.gen.next()
						adj = self.gen.next()
						adj.color = Cyan
						
						self.jump.set_volume(.1)
						self.jump.play()
						pygame.time.wait(self.delay)					
						
						if(self.current is not self.start):
							self.current._color = Silver
							
					except StopIteration:
						for i in self.algo.PATH:								
							if i is not self.start:
								i._color = Lime
						
						print("finished")
						for i in self.audioclips: i.stop()
						self.fin.set_volume(.15)
						self.fin.play()
						
						self.gen = None
						#start = goal
			else:
				bg.blit(self.font2.render("PAUSED", True, White), textrect.move(5,10))
				bg.blit(self.font2.render("Press F to unpause", True, White), textrect.move(5, 35))
				bg.blit(self.font2.render("Left click to add new blockers", True, White), textrect.move(5,60))
				bg.blit(self.font2.render("Right click to set starting position!", True, White), textrect.move(5, 85))
				bg.blit(self.font2.render("Try to block off the bad guy!", True, White), textrect.move(5, 110))
				self.screen.blit(bg, (0,0))
			if(debug):					
				debugText = self.font2.render("DEBUG", True, White)				
				self.screen.blit(debugText,(0,0))
				
			pygame.display.flip()
	
		pygame.quit()
		
		
if __name__ == '__main__': 
	Game().run()
	

