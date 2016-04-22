import pygame
import math
white = (255,255,255)
black = (0,0,0)
class Node(object):
	
	def __init__(self, x, y, id):		
		#MANUAL SIZE
		
		SIZE = 50
		self.width = SIZE
		self.height = SIZE
		self.id = id
		self.x = (5 + self.width) * x + 5
		self.y = (5 + self.height) * y + 5
		self.pos = (self.width * x, self.height * y)		
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
		self.parent = None		

		self.walkable = True
	
		self.dirty = False
		white = (255,255,255)
		self._color = white
		
		#position is x goes right
		# y goes down so 
		
		self.f = None
		self.g = None
		self.h = None
		
	@property
	def color(self):
		return self._color
	
	@color.setter
	def color(self, value):
		#print("set dirty")
		self.dirty = True
		self._color = value
	
	#properties	
	
	
	def draw(self, screen, font):		
		if not self.walkable: 
			self._color = (255,0,0)
		
		#create some text to go on the fill
		
		#info to display
		info = str((self.id))
		#render the text
		text = font.render(info, 1, (1, 1, 1))
		#set it's position/parent
		textpos = self.rect
		#center it
		textpos.centerx = self.rect.centerx
		
		
		#draw the square
		pygame.draw.rect(screen, self._color, self.rect)
		#screen.fill(self._color, self.rect)
		#blit the text 
		screen.blit(text, textpos)
		
	def getF(self):
		return self.h + self.g
	def setH(self, val):
		self.h = val
	def setG(self, val):
		self.g = val
	def onclick(self, pos):	
		 
		oldColor = self.color
		newColor = (255,0,255)
		#if we have set it's color manually then it is dirty so ignore it
		if not self.dirty:			
			x = pos[0]
			y = pos[1]		
			#if we click in this square set it's color
			if(x > self.rect.left and x < self.rect.right and y >self.rect.top and y < self.rect.bottom):
				print("clicked on square at ", self.rect)
				self._color = newColor
			#if this isn't the square we clicked then set it back to the original
			else:
				self._color = white
		
		
		
		
		

class Astar:
	def __init__(self, SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []		
	
	def Run(self):
		self.OPEN.append(Start)
		while not self.OPEN:
			current = self.LowestF(self.OPEN)			


		
'''
	TODO.Add(start)


	while (!TODO.IsEmpty())	// While there are squares to check
	{
		current = TODO.LowestF() // Get the lowest F
		TODO.Remove(current) 
		DONE.Add(current)

		foreach (adjacent square)
		{
			if (square.walkable && !DONE.Contains(square))
			{
				if (!TODO.Contains(square))
				{

					if (square.IsDestination())
					{
						RetracePath();
						return true; // Success
					}

					else
					{
						TODO.Add(square);
					
						square.Parent = current;
						// calcuate G and H
					}
				}

				else
				{
					int costToMoveToSquare = current.G + costToMove;

					if (costToMoveToSquare < square.G)
					{
						square.Parent = current;
						square.G = costToMoveToSquare;
						TODO.Sort();
					}
				}
			}
		}
	}

	return false; // Failure
	'''




