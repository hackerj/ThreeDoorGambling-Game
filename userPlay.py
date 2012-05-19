"""
 ---------------
 Let's Make A Deal
 ---------------
 Authors: Jessie Liu, CMC; Szeyin Lee, PO; Siyao Xie, PO
 Version: 0.1 using Python 2.7, Pygame
"""
import pygame, os, sys, math, random
from pygame.locals import *
from random import *

class UserPlay:
    def __init__(self):
        """Initial scenario 2 game play"""
        
        self.switch = 1 # prob. to swith, by default always swith
        self.win = 0 # num winning
        self.trials = 0 # num trials

        # start playing
        self.startGame()

    def startGame(self):
        print "starting user play"
