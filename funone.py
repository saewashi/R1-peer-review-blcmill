#!/usr/bin/env python
'''

For this exercise, draw a circle wherever the user clicks the mouse

'''
import sys, pygame
import random
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
    colorCycle = 1
    radius = 20

    while True:
        clock.tick(FPS)
        pos = (random.randrange(800), random.randrange(600)) #random position
        if (colorCycle % 5 == 0): # depending on mouse click, execute one of these
        #COLORS ARE DETERMINED BY POSITION
            color = (255, 255 * pos[0]/800, 255 * pos[1]/600) #Colorscheme 1
        elif (colorCycle % 5 == 1):
            color = (255 * pos[0]/800 , 255, 255 * pos[1]/600) #Colorscheme 2
        elif (colorCycle % 5 == 2):
            color = (255 * pos[0]/800 , 255 * pos[1]/600, 255) #Colorscheme 3
        elif (colorCycle % 5 == 3):
            color = (0, 0, 0) #Colorscheme 4 (black)
        elif (colorCycle % 5 == 4):
            color = (255 * pos[0]/800, 255 * pos[0]/800, 255 * pos[0]/800) #Colorscheme 5 (B&W Gradient)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                colorCycle += 1 #Change color

        pygame.draw.circle(screen, color, pos, radius) #It also changes color!

        pygame.display.flip()

if __name__ == '__main__':
	main()
