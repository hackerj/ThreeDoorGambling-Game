"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, SCR; Siyao Xie, PO
 Version: 2.0 using Python 2.7, Pygame 1.9
"""


import pygame, pygame.font, pygame.event, pygame.draw, pygame.key, string
from pygame.locals import *
from menuHandler import MenuHandler
from game import Game


class EventHandler:    
    MENU = 0
    AUTO1 = 1
    AUTO2 = 2
    USERPLAY =3

    
    def __init__(self,menu):
        """initializes EventHandler"""
        
        self.game = None
        self.moreInput = False
        self.trials = True # This is the input box for numTrials
        self.mode = self.MENU
        self.menu = menu
        

    def processMenuClick(self, (x,y)):
        """which button player choose?"""
        
        for buttons in self.menu.block:
            if (buttons["rect"].collidepoint(x,y)):
                print "You are playing Game ",`buttons['name']`
	        self.mode = buttons['name']
	        # start whatever game
	        self.game=Game(self.mode)
            else:
                pass

            
    def processKeyEvent(self,key, dialog):
        """Event for dialog input"""
        valid_key = [K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9]
        valid_key2 = [K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9, K_PERIOD]
        
        if dialog ==0:
            if key == K_BACKSPACE:
                self.game.string = self.game.string[0:-1]

            elif key== K_RETURN:
                self.moreInput = False
                self.trials == False
                self.game.numTrials = int(string.join(self.game.string,""))
                print "num of trials in the game is ", self.game.numTrials
                if self.mode == self.AUTO1:
                    self.game.startAuto1()
                return
            elif key in valid_key:
                inkey = pygame.key.name(key)
                self.game.string.append(inkey)
                self.game.display_box(self.game.screen, string.join(self.game.string,""),1)
                self.game.numTrials = int(string.join(self.game.string,""))
            else: 
                return
            
        else:
            if key == K_BACKSPACE:
                self.game.probString = self.game.probString[0:-1]
                self.game.display_box(self.game.screen, string.join(self.game.probString,""),4)                

            elif key== K_RETURN:
                self.game.prob = float(string.join(self.game.probString,""))
                self.moreInput = False
                print "prob of the game is", self.game.prob
                self.game.startAuto2()
                
                return
            elif key in valid_key2:
                inkey = pygame.key.name(key)
                self.game.probString.append(inkey)
                self.game.display_box(self.game.screen, string.join(self.game.probString,""),4)
                self.game.prob = float(string.join(self.game.probString,""))
                            
        
       
   
