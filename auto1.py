"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, SCR; Siyao Xie, PO
 Version: 2.0 using Python 2.7, Pygame 1.9
 
"""

import pygame, os, sys
from pygame.locals import *
from random import *


class Auto1:
    def __init__(self, numTrials):
        """Initial scenario 2 game play"""
        
        self.winSwitch = 0.0 # num winning if switch
        self.winNotSwitch = 0.0 # num winning if switch
        self.trials = numTrials # num trials

        # For message display
        self.switchResultText = []
        self.notSwitchText = []
        
        # start playing
        self.startGame()
        

    def startGame(self):
        # two types of people: always switch or not switch
        self.gameSwitch()
        self.gameNotSwitch()


    def gameSwitch(self):
        """Scenarios when player ALWAYS decides to switch"""
        n = 0 
        while n < self.trials:
            # choose a number from 0 to 2
            gift = randrange(0,3)
            contest = randrange(0,3)
            
            # Player always lose if switch when choose the right
            # gift in the first place
            if gift == contest:
                pass
            
            # if player currently choose the wrong one, and since the
            # host reveals another one, player will always win by switching
            else:
                self.winSwitch +=1
            n+=1
            
        white = 5*" "
        self.switchResultText = ["Trials"+ white + "Num of Winning" + white + "Prob of Winning with switching",
                              `self.trials` + 2*white + `self.winSwitch` + 5*white + `self.winSwitch/self.trials`]

        print "\n"
        print "SWITCHING..."
        print "num of wins is: ", self.winSwitch
        print "num of trials is: ", self.trials
        print "prob. to win with switch is: ", self.winSwitch/self.trials
        print "\n"


        
                
    def gameNotSwitch(self):
        """Scenarios when player decides not to switch"""
        n = 0 
        while n < self.trials:
            gift = randrange(0,3)
            contest = randrange(0,3)
            
            # player win regardless because he doesn't switch
            if (gift==contest):
                self.winNotSwitch +=1
            # lose if player dont switch
            else:
                pass
            n+=1

        white = 5*" "
        self.notSwitchText = ["Trials"+ white + "Num of Winning" + white + "Prob of Winning w/o switching",
                              `self.trials` + 2*white + `self.winNotSwitch` +5* white + `self.winNotSwitch/self.trials`]        

        # output statment to the game screen.
        print "NOT SWITCHING..."
        print "num of wins is: ", self.winNotSwitch
        print "num of trials is: ", self.trials        
        print "prob. to win without switch is: ", self.winNotSwitch/self.trials
        print "\n"

                
        
        
    
