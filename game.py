"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, SCR; Siyao Xie, PO
 Version: 2.0 using Python 2.7, Pygame 1.9
"""


import pygame, os, sys, math, random
import pygame.font, pygame.event, pygame.draw,string
from pygame.locals import *
from auto2 import Auto2
from auto1 import Auto1
from userPlay import UserPlay


# Should be able to choose different games to play
class Game:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255,255,0)
    WHITE = (255,255,255)
    
    def __init__(self,gameNum):
        self.gameNum = gameNum # game to play

        # graphic settings
        self.back = None # back to main menu button setting
        self.screen = None # background setting
        
        # user input to dialog box
        self.string = [] # for taking num input
        self.numTrials = 0 # num of trials to test
        self.prob = 0.0 # prob for auto 2
        self.probString = [] # for taking string input

        # games
        self.auto2 = None # game 2
        self.auto1 = None # game 1
        
        # player finish game play
        self.done = False

        # start playing!
        self.playGame()
        
        
    def playGame(self):
        
        if (self.gameNum ==1):
            self.autoGraphic(self.gameNum)
        elif (self.gameNum ==2):
            self.autoGraphic(self.gameNum)
            
        elif (self.gameNum ==3):
            self.userGraphic()
            game = UserPlay()
        else:
            print "Invalid input in playGame"

            
    def autoGraphic(self,num):
        """Graphic init for auto games."""
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill(self.BLACK)
        self.back = {'rect':pygame.Rect(30,560, 100, 30), 'color':self.BLUE}
        pygame.draw.rect(self.screen, self.back['color'], self.back['rect'])

        background= pygame.image.load("bg.bmp")
        self.screen.blit(background, (0,0))
       
        pygame.font.init()
    	font = pygame.font.Font(None, 25)
    	text = font.render("MAIN MENU", 1, self.WHITE)
    	textPos = (30,560)
	self.screen.blit(text, textPos)

        
        # DIALOG BOX!
        self.dialog = {'rect':pygame.Rect(286,280,218,50)}
        pygame.draw.rect(self.screen, self.RED,
                   self.dialog['rect'], 0)


        g1box= pygame.image.load("g1box.bmp")
        self.screen.blit(g1box, (283,205))
        
        if num ==1:
            pygame.display.set_caption("Gamble 1")
        elif num ==2:
            pygame.display.set_caption("Gamble 2")
            
            self.dialog2 = {'rect':pygame.Rect(286,425,218,50)}
            pygame.draw.rect(self.screen, self.BLUE,
                   self.dialog2['rect'], 0)

            g2box= pygame.image.load("g2box.bmp")
            self.screen.blit(g2box, (283,350))


        else:
            print "invalid game number!"
            return
        pygame.display.update()


    def display_box(self,screen,message, num):
        """Draw dialog box and take in inputs"""
        if len(message) > 0 and num==0:
            fontobject = pygame.font.Font(None,25)
            self.screen.blit(fontobject.render(message, 1, (255,255,255)),
                (295,290)) #(300,280,218,50)
            pygame.display.flip()
        elif len(message) > 0 and num==1:
            fontobject = pygame.font.Font(None,25)

            # dialog box property
            self.screen.blit(fontobject.render(message, 1, (255,255,255)),
                (295,290)) 
            pygame.display.flip()
            
           
        elif len(message) > 0 and num==3:
            fontobject = pygame.font.Font(None,25)
            self.screen.blit(fontobject.render(message, 1, (255,255,255)),
                (295,430)) 
            pygame.display.flip()
            
        elif len(message) > 0 and num==4:
            fontobject = pygame.font.Font(None,25)
            self.screen.blit(fontobject.render(message, 1, (255,255,255)),
                (295,430))
            pygame.display.flip()

                
    def startAuto1(self):
        """Start first game play"""
        self.auto1 = Auto1(self.numTrials)
        self.drawResults()
            
    def startAuto2(self):
        """Start second game play"""
        self.auto2 = Auto2(self.numTrials, self.prob)
        self.drawResults()

    def drawResults(self):
        """Output results after game play finish"""
        pygame.font.init()

        # popup result
    	font = pygame.font.Font(None, 36)
        self.screen.fill((130,174,202),(50,50,700,500))
        text = "Test Results"
        text_rendered = font.render(text,1,self.WHITE)
        self.screen.blit(text_rendered,(250,100))
        
        font1 = pygame.font.Font(None, 25)
        if self.auto2:
            result = self.auto2.switchResultText + ["break"] + self.auto2.notSwitchText
        elif self.auto1:
            result = self.auto1.switchResultText+["break"] +  self.auto1.notSwitchText
        else:
            pass
        
        n = 0
        while result:
            text = result[0]
            if text == "break":
                n+=4
            else:
                display = font1.render(text, 1, self.WHITE)
                self.screen.blit(display, (150, 200+n*15))
                n+=2
                
            result = result[1:]
        pygame.display.flip()

        # After game is finished, player is presented oppotunity to
        # play again.
        self.playAgain()
        
    def playAgain(self):
        """draw play again box and be able to restart the same game"""
        # player finish the game!
        self.done = True

        # play again box
        self.again = {'rect':pygame.Rect(650, 560, 200, 30), 'color':self.WHITE}
        pygame.font.init()
    	font = pygame.font.Font(None, 25)
    	text = font.render("PLAY AGAIN!", 1, self.WHITE)
    	textPos = (650,560)
	self.screen.blit(text, textPos)
	
	# Update graphic
        pygame.display.flip()

        
        
    def userGraphic(self):
        """Graphic for user play..(NOT IMPLEMENTED YET)"""
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill(self.BLACK)
        self.back = {'rect':pygame.Rect(500, 528, 200, 30), 'color':self.BLUE}
        pygame.draw.rect(self.screen, self.back['color'], self.back['rect'])
        
        pygame.font.init()
    	font = pygame.font.Font(None, 36)
    	text = font.render("BACK TO MAIN", 1, self.WHITE, self.BLUE)
    	self.backToM = text.get_rect()
	self.screen.blit(text, (500,530))
	pygame.display.update()

        print "Initializing user Graphic"
        
        
        
