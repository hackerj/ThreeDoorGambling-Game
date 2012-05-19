"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, SCR; Siyao Xie, PO
 Version: 2.0 using Python 2.7, Pygame 1.9
"""


import pygame, os, sys, math, random
from pygame.locals import *
from menuHandler import MenuHandler
from eventHandler import EventHandler
from game import Game

WHITE = (255,255,255)

class Main:
    #magic numbers
    MENU = 0
    AUTO1 = 1
    AUTO2 = 2
    USERPLAY =3
    
    def __init__(self):
        self.mode = self.MENU
        self.menu = None
        self.main()
        
        
    def main(self):
        # init game and graphic
        pygame.init()
        pygame.display.init()
        
        # init menu and event taken
        self.menu = MenuHandler()
        handler = EventHandler(self.menu)
        
        while True:
            # handle all the user inputs...
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise SystemExit

                if event.type == MOUSEBUTTONUP:
                    if handler.mode == self.MENU:
                        handler.processMenuClick(pygame.mouse.get_pos())
                        
                    # handle back to menu event
                    elif handler.game.back['rect'].collidepoint(pygame.mouse.get_pos()):
                        self.menu = MenuHandler()
                        handler = EventHandler(self.menu)

                    elif handler.game.done:
                        if handler.game.again['rect'].collidepoint(pygame.mouse.get_pos()):
                            handler.game.done = False
                            handler.game=Game(handler.mode)
                    
                    elif handler.mode ==self.AUTO1:
                        if handler.game.dialog['rect'].collidepoint(pygame.mouse.get_pos()):
                            handler.moreInput = True
                            handler.trials = True
                        else:
                            pass
                    elif handler.mode ==self.AUTO2:
                        if handler.game.dialog['rect'].collidepoint(pygame.mouse.get_pos()):
                            handler.moreInput = True
                            handler.trials = True
                        elif handler.game.dialog2['rect'].collidepoint(pygame.mouse.get_pos()):
                            handler.moreInput = True
                            handler.trials = False

                            
                        else:
                            pass

                if event.type == KEYDOWN and handler.moreInput:
                    if handler.mode == self.AUTO1 or handler.mode ==self.AUTO2:
                        if handler.trials == True:
                            handler.processKeyEvent(event.key,0)
                        elif handler.trials == False:
                            handler.processKeyEvent(event.key,1)
                        
                else:
                    pass

            


if __name__ == "__main__":
    app = Main()
    
