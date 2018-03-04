#!/usr/bin/env python
'''

For this exercise, draw a circle wherever the user clicks the mouse

'''
import sys, pygame
from datetime import datetime
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	font = pygame.font.SysFont("arial",64)
	clock = pygame.time.Clock()

	(x,y,radius) = (100,100,20)
	pos = (100, 100) #you have to initialize pos here before setting it
	screen.fill(black)
	
	while True:
		clock.tick(FPS)

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
		
		pygame.draw.circle(screen,
                                   ((int(pos[0]) * 255) / screen_size[0],
                                    (int(pos[1] * 255) / screen_size[1]),
                                    255), pos, radius) #It also changes color!
		
		pygame.display.flip()

if __name__ == '__main__':
	main()
