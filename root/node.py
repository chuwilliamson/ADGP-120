import pygame
import math

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
class Node(object):
	
	def __init__(self, x, y, id):		
		#astar vars
		self.adjacents = []	
			#bottom = id + 1
			#top = id - 1
			#right = id + rows
			#left = id - rows
			#top_right = id + rows - 1
			#top_left = id - rows + 1
			#bot_left = id - rows - 1
			#bot right = id + rows -1
		self.parent = None		
		self._walkable = True	
		self._g = 0
		self._h = 0
		self._f = 0
		
		#drawing vars
		SIZE = 30		
		self.width = SIZE
		self.height = SIZE
		self.id = id
		self.index = (x,y)
		self.x = (5 + self.width) * x + 5
		self.y = (5 + self.height) * y + 5
		self.pos = (self.width * x, self.height * y)
		self.screenpos = (self.x, self.y)		
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)		
		self.surface = pygame.Surface((self.width, self.height))
		self.dirty = False		
		self._color = White		
		

	#properties	
	@property
	def walkable(self):
		return self._walkable
	@walkable.setter
	def walkable(self, value):
		white = (255,255,255)
		red = (255,0,0)
		self._walkable = value	
		#if it's set to walkable change to white
		#this will mark it as undirty
		if value:
			self.color = (255,255,255)						
		else:
			self.color = (255,0,0)		
			
		
			
		
	@property
	def f(self):
		return self._f
	@property
	def g(self):
		return self._g
	@property
	def h(self):
		return self._h
	
	@f.setter
	def f(self,value):
		self._f = value
	@g.setter
	def g(self, value):
		self._g = value
		self._f = self._g + self._h
		
	@h.setter
	def h(self, value):
		self._h = value
		self._f = self._g + self._h
	
	@property
	def color(self):
		return self._color
	
	@color.setter
	#manual setting of colors will mark them dirty so they will stay
	def color(self, value):	
		white = (255,255,255)
		red = (255,0,0)
		
		if value is red:
			self._color = value
			self.dirty = True
		else:
			self._color = value
			
		
		
			
		self._color = value
	def info(self):
		print("pos = ", self.pos)
		ids = ""
		for i in self.adjacents:			
			ids += " " + str(i.id)			
		print("neighbors:", ids)
		print("index: ", self.index)
	
	def draw(self, screen, font, init = True, text = True):		
		#pygame.draw.rect(screen, self._color, self.rect)
		self.surface.fill(self._color)
		screen.blit(self.surface, self.screenpos)
		if self.walkable:
			#create some text to go on the fill
			
			#info to display
			
			#render the text
			
			textf = font.render("F= " + str(self.f), True, (1, 1, 1))
			textg = font.render("G= " + str(self.g) + "H= " + str(self.h), True, (1, 1, 1))
			#texth = font.render("h= " + str(self.h), True, (1, 1, 1))
			#set it's position/parent
			textfpos = (self.x, self.y) #top left
			textgpos = (self.x, self.y + self.height - 10) #bot left		
			#texthpos = ((self.x + self.width /2 ) + len("H= " + str(self.h))  , self.y + self.height - 10)
			#center it
			
			#draw the square
			if init and text:				
				screen.blit(textf, textfpos)
				screen.blit(textg, textgpos)
			#	screen.blit(texth, texthpos)
		
			
		
		
	
		
		
		
		
	
	def onclick(self, pos):	
		oldColor = self.color
		newColor = (255,0,255)
		#if we have set it's color manually then it is dirty so ignore it
		x = pos[0]
		y = pos[1]
		o = None
		#if we click in this square set it's color
		if(x > self.rect.left and x < self.rect.right and y >self.rect.top and y < self.rect.bottom):			
			if not self.dirty: #if we didn't set it's color manual
				self._color = newColor
			o = self
			
		return o
		
			
					
		
		
		
		
		
