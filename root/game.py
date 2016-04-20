"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import math,pygame
from astar import *



def mag(a):
	return math.sqrt(a[0]^2 + a[1]^2)
	
def main():
	Red = (255,255,255)
	Grn = (0,255,0)        
	print("mag of 255,255", mag((255,255)))
	#create the search space to look through
	searchSpace = []
	for x in range(10):
		for y in range(10):
			n = Node(x, y)
			#x goes right
			#y goes down
			unwalkable = True if (x >= 5 and x <= 6 and y >= 5 and y <= 8) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			
			n.setWalk(unwalkable)
			searchSpace.append(n)
			

	# Initialize pygame
	pygame.init()
	# Initialize fonts
	pygame.font.init()
	# Set the HEIGHT and WIDTH of the screen
	screen_width = 1000
	screen_height = 1000
	# Set the screen
	screen = pygame.display.set_mode([screen_width, screen_height])

	# Set title of screen
	pygame.display.set_caption("Astar")


	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	
	 
	Running = True
	# -------- Main Program Loop -----------
	while Running:
		clicked = (0,0)
		for event in pygame.event.get():  # User did something			
			if event.type == pygame.MOUSEBUTTONDOWN:
				clicked = pygame.mouse.get_pos()
			if event.type == pygame.QUIT:
				Running = False
		
		if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
			Running = False
			
		for i in searchSpace:
			i.draw(screen, Red)
		
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()

