"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, SCR; Siyao Xie, PO
 Version: 2.0 using Python 2.7, Pygame 1.9
"""

import pygame, os, sys, math, random
from pygame.locals import *

# Should be able to choose different games to place

class MenuHandler:
    # Magic numbers
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255,255,0)
    WHITE = (255,255,255)

    def __init__(self):
        """Initial the menuHandler"""
        self.gamePlay = 0
	self.background = None
	self.block = []  # store all the buttons
	self.draw() # draw graphics
	
    def draw(self):

        # initialize screen
	menuScreen = pygame.display.set_mode((800, 600))
    	pygame.display.set_caption("Gambling Game")
    	menuScreen.fill(self.BLACK)
        background= pygame.image.load("bg.bmp")
        menuScreen.blit(background, (0,0))

	# buttons set up
        b1 = {'rect':pygame.Rect(300, 250, 200, 50), 'color':self.RED, 'name':1}
        b2 = {'rect':pygame.Rect(300, 350, 200, 50), 'color':self.BLUE, 'name':2}
        #b3 = {'rect':pygame.Rect(300, 450, 200, 50), 'color':self.GREEN, 'name':3}
        self.block = [b1,b2]
        
        for b in self.block:
            pygame.draw.rect(menuScreen, b['color'], b['rect'])
        
        print "Hi, Welcome to Jumbo Gambling! Please choose a game to play."



        # Image loaded
        game1 = pygame.image.load("red.bmp")
        menuScreen.blit(game1, (300,210))

        game2 = pygame.image.load("blue.bmp")
        menuScreen.blit(game2, (300,310))

        # display image
        pygame.display.update()



