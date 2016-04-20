#Add the starting square (or node) to the open list.
import pygame

#pygame.init()
#screen = pygame.display.set_mode((640,480))

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
print 'how do i make a game?'
window = 0											   # glut window number
width, height = 500, 400							   # window size

class Node:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.parent = None
	def draw(self):
		glColor3f(0.0, 0.0, 1.0)						   # set color to blue
		glBegin(GL_QUADS)								   # start drawing a rectangle
		glVertex2f(self.x, self.y)								   # bottom left point
		glVertex2f(self.x + self.width, self.y)						   # bottom right point
		glVertex2f(self.x + self.width, self.y + self.height)				   # top right point
		glVertex2f(self.x, self.y + self.height)						   # top left point
		glEnd()
		glColor3f(1.0, 0.0, 0.0)	
		glBegin(GL_LINES)		
		glVertex2f(self.x,self.y)
		if(self.parent is None):
			glVertex2f(height/2, width/2)
		else:		
			glVertex2f(parent.x, parent.y)
		glEnd()
		
def refresh2d(width, height):
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	glMatrixMode (GL_MODELVIEW)
	glLoadIdentity()


def draw():											   # ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()								   # reset position
	refresh2d(width,height)
	# ToDo draw rectangle
	n1 =  Node(10, 10, 200, 100)
	n1.draw()
	n2 = Node(250, 250, 100, 50)
	n2.draw()
	
	glutSwapBuffers()								   # important for double buffering

# initialization
glutInit()											   # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)					   # set window size
glutInitWindowPosition(0, 0)						   # set window position
window = glutCreateWindow("PyOpenGL")			                    # create window with title
glutDisplayFunc(draw)								   # set draw function callback
glutIdleFunc(draw)									   # draw all the time
glutMainLoop()




'''	   


#while(True):
	   # if(openlist.empty):
		 #		 print("no path")
  #		 break
   #	 elif(closedlist.contains(targetSquare)):
	   # print("path found")
	#	 break
	 #	 else:
	
	
	#setup your search area
	#draw the picture
	#how do i get from the green to the red?
	#there be a wall in between...
	
	#Once we have simplified our search area into a manageable number of nodes, as we have done with the grid layout above, the next step is to conduct a search to find the shortest path. 
	#We do this by starting at point A, 
	#checking the adjacent squares, 
	#and generally searching outward until we find our target. 
	
	#1.
	#Begin at A and add it to an "open list" of squares to be considered.
	#open list is a list of potentital nodes we can go to.
	#The items in this list MIGHT fall along the path you want to take, but maybe not.
	#Basically a list of squares that need to be checked out
	
	#2.
	#Look at all the reachable or walkable squares adjacent to A and add them to the open List
	##Important!
	#save point A as their parent
	#need this to retrace path
	
	#3.
	#Drop the starting square from openList and add it to closed list of squares that we don't need to look at anymore
	
	#4.
	#Choose one of the adjacent squares on the open list and repeat
	#Which to choose? lowest F cost!
	#What is F?
	#F = G + H
	#G = the movement cost to move from the starting point A to a given square on the grid, following the path generated to get there
	#H = the estimated movement cost to move from that given square on the grid to the final destination, point B.
	


	'''
