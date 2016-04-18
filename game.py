"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
from astar import *



def main():


	# Create a 2 dimensional array. A two dimensional
	# array is simply a list of lists.
	searchSpace = []
	for i in range(10):
		for j in range(10):
			n = Node(i, j)
			searchSpace.append(n)

	# Initialize pygame
	pygame.init()

	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [255, 255]
	screen = pygame.display.set_mode(WINDOW_SIZE)

	# Set title of screen
	pygame.display.set_caption("Astar")

	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()



	# -------- Main Program Loop -----------
	while not done:
		for event in pygame.event.get():  # User did something
			if event.type == pygame.QUIT:  # If user clicked close
				done = True	 # Flag that we are done so we exit this loop




		# Set the screen background
		screen.fill((0,0,0))

		for i in searchSpace:
			i.draw(screen, (255,255,255))

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()

