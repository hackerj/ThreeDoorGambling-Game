"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, SCR; Siyao Xie, PO
 Version: 2.0 using Python 2.7, Pygame 1.9
 
"""

import pygame, os, sys, math
from pygame.locals import *
from random import *

class Auto2:
    def __init__(self, numTrials, prob):
        """Initial scenario 2 game play"""
        
        self.winSwitch = 0.0 # num winning
        self.winNotSwitch = 0.0
        self.trials = numTrials # num trials
        self.prob = prob # prob for host to open the door
        self.switchText = []
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
            player = randrange(0,3)

            # If player picked the right one, but always switch after
            # the host open curtain, the player loses regardless.
            if gift == player:
                pass
            
            else:
                chance = uniform(0,1)
                
                # The host open the curtain, player lose because
                # he selects the wrong one.
                if chance<=self.prob:
                    pass
                else:
                    self.winSwitch +=1
            n+=1
            
        
        white = 5*" "
        self.switchResultText = ["Trials"+ white + "Num of Winning" + white + "Prob of Winning with switching",
                              `self.trials` + 2*white + `self.winSwitch` + 5*white + `self.winSwitch/self.trials`]


        
        print "num of winnings with switch is: ", self.winSwitch
        print "num of trials is: ", self.trials
        print "prob to win with switch is: ", self.winSwitch/self.trials
                    

    def gameNotSwitch(self):
        """Scenarios when player decides not to switch"""
        n = 0 
        while n < self.trials:
            gift = randrange(0,3)
            player = randrange(0,3)
            
            # If not switch, you always win if player pick the right gift
            # at the first time.
            if gift == player:
                self.winNotSwitch +=1
                
            # lose regardless if didnt pick the right gift since player
            # wont switch.
            else:
                pass
            
            n+=1


        # output statment to the game screen.
        white = 5*" "
        self.notSwitchText = ["Trials"+ white + "Num of Winning" + white + "Prob of Winning w/o switching",
                              `self.trials` + 2*white + `self.winNotSwitch` +5* white + `self.winNotSwitch/self.trials`]
        
        print "\nnum of winnings without switch is: ", self.winNotSwitch
        print "num of trials is: ", self.trials        
        print "prob to win without switch is: ", self.winNotSwitch/self.trials
                   
                    
      
                
                
