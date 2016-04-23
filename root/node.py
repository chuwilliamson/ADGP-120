import pygame
import math
white = (255,255,255)
black = (0,0,0)
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
		self.walkable = True	
		self._g = 0
		self._h = 0
		self._f = 0
		
		#drawing vars
		SIZE = 60		
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
		self._color = white		
		

	#properties	
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
	def color(self, value):		
		self.dirty = True
		self._color = value
		if(value == white):
			self.dirty = False
	
	
	def info(self):
		print("pos = ", self.pos)
		ids = ""
		for i in self.adjacents:			
			ids += " " + str(i.id)			
		print("neighbors:", ids)
		print("index: ", self.index)
	
	def draw(self, screen, font, init = True):		
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
			if init:				
				screen.blit(textf, textfpos)
				screen.blit(textg, textgpos)
			#	screen.blit(texth, texthpos)
		else:			
			self.color = (255,0,0)
			
		
		
	
		
		
		
		
	
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
				#for i in self.adjacents:
					#if not i.dirty:
						#i._color = (125, 125, 125)
			o = self
			
		return o
				
				
			#if this isn't the square we clicked then set it back to the original
		
			
					
		
		
		
		
		
