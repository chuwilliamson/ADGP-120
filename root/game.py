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


white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
teal = (128, 128, 255)
def mag(a):
	return math.sqrt(a[0]^2 + a[1]^2)
	
def main():
	
	Red = (255,255,255)
	Green = (0,255,0)     
	Yellow = (255,255,0)	
	print("mag of 255,255", mag((255,255)))
	#create the search space to look through
	mouse_listeners = []
	search_space = {}
	id = 0
	for x in range(15):
		for y in range(15):
		
			n = Node(x, y, id)
			#x goes right
			#y goes down
			if (x >= 5 and x <= 6 and y >= 5 and y <= 8):
				n.walkable = False
			if(x % 15 == 0 or y % 15 == (15 - 1) or x % 15 == 14 or y % 15 == 0):
				n.walkable = False
				
			mouse_listeners.append(n.onclick)
			
			search_space[id] = n
			id+=1
		

	# Initialize pygame
	pygame.init()
	# Initialize fonts
	pygame.font.init()
	# Set the HEIGHT and WIDTH of the screen
	screen_width = 830
	screen_height = 850
	# Set the screen
	screen = pygame.display.set_mode([screen_width, screen_height])
	font = pygame.font.Font(None, 15)
	# Set title of screen
	pygame.display.set_caption("Astar")


	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()
	start = search_space[28]
	start.color = teal 
	goal = search_space[196]
	goal.color = green
	Astar(search_space, start, goal )
	Running = True
	# -------- Main Program Loop -----------
	while Running:		
		
		for event in pygame.event.get():  # User did something			
			if event.type == pygame.MOUSEBUTTONDOWN:
				for i in search_space:
					if not search_space[i].dirty:
						search_space[i].color = white
				for callback in mouse_listeners:
					callback(pygame.mouse.get_pos())
				
				
			if event.type == pygame.QUIT:
				Running = False
		
		if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
			Running = False
			
		for i in search_space:
			search_space[i].draw(screen, font)
		
		clock.tick(60)
			
		
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()

