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
		self.g = 9000
		self.h = 9000
		self.f = self.g + self.h
		
		#drawing vars
		SIZE = 50		
		self.width = SIZE
		self.height = SIZE
		self.id = id
		self.x = (5 + self.width) * x + 5
		self.y = (5 + self.height) * y + 5
		self.pos = (self.width * x, self.height * y)		
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)		
		
		self.dirty = False		
		self._color = white		
		

		
		
	@property
	def color(self):
		return self._color
	
	@color.setter
	def color(self, value):
		#print("set dirty")
		self.dirty = True
		self._color = value
		if(value == white):
			self.dirty = False
	
	#properties	
	def info(self):
		print("pos = ", self.pos)
		ids = ""
		for i in self.adjacents:			
			ids += " " + str(i.id)
			
		print("neighbors = ", ids)
	
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
				self.info()
				self._color = newColor
				for i in self.adjacents:
					i._color = (125, 125, 125)
				
			#if this isn't the square we clicked then set it back to the original
		
			
					
		
		
		
		
		

class Astar:
	def __init__(self, SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []
		self.graph = SearchSpace
		for n in self.graph:
			 self.SetNeighbors(self.graph[n])
		
			
	
	def Run(self):
		open = self.OPEN
		closed = self.CLOSED
		open.append(start)
		while not open:
			current = open.sort(key = lambda x : x.f)[0]
			open.remove(current)
			closed.append(current)
			
	def SetNeighbors(self, node):
	#always use rows b/c we go nxn
		rows = 15
		bot = node.id + 1
		top = node.id - 1
		right = node.id + rows
		left = node.id - rows
		t_right = right - 1
		t_left = left - 1
		b_right = right + 1
		b_left = left + 1
		adjs = [bot, top, right, left, b_right, b_left, t_right, t_left ]
		for i in adjs:
			if i in self.graph:
				if self.graph[i].walkable:
					node.adjacents.append(self.graph[i])
				
	
		
		
		
	


		
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




