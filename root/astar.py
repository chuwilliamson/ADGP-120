import pygame as gfx
class Node:
	def __init__(self, x, y):
		self.parent = None		
		self.color = (255,255,255)
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x, self.height - y)
		self.f = None
		self.g = None
		self.h = None

	def draw(self, screen, color):
		margin = self.margin
		color = (0, 0, 255) if (self.walkable) else (255,0,0)
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
		
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




