import pygame
import math
class Node:
	def __init__(self, x, y):		
		#MANUAL SIZE
		#nxn
		SIZE = 50
		self.width = SIZE
		self.height = SIZE
		
		self.x = (5 + self.width) * x + 5
		self.y = (5 + self.width) * y + 5
		self.pos = (self.x, self.y)		
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
		
		self.parent = None		

		self.color = (126,126,255)

		self.walkable = True
		#position is x goes right
		# y goes down so 
		
		self.f = None
		self.g = None
		self.h = None

	def draw(self, screen, color):		
		color = (0, 0, 255) if (self.walkable) else (255,0,0)
		width = screen.get_size()[0]
		self.rect[2] =  math.sqrt(width) * 2 
		height = screen.get_size()[1]	
		self.rect[3] =  math.sqrt(height) * 2
		#create some text to go on the fill
		font = pygame.font.Font(None, 15)
		#info to display
		info = str(self.x) + " , " + str(self.y)
		#render the text
		text = font.render( info, 1, (1, 1, 1))
		#set it's position/parent
		textpos = self.rect
		#center it
		textpos.centerx = self.rect.centerx
		#draw the square
		screen.fill(color,self.rect)
		#blit the text 
		screen.blit(text, textpos)
		
		
		
	def setWalk(self, walkable):
		self.walkable = walkable
		 
	def getF(self):
		return self.h + self.g
	def setH(self, val):
		self.h = val
	def setG(self, val):
		self.g = val

class Astar:
	def __init__(self, SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []		
	
	def Run(self):
		self.OPEN.append(Start)
		while not self.OPEN:
			current = self.LowestF(self.OPEN)
			
	def LowestF(self, Nodes):
		lowestF = -1
		nodeWithLowestF = None
		for node in Nodes:
			if(node.f > lowestF):
				lowestF = node.f
				nodeWithLowestF = node
		return nodeWithLowestF
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




