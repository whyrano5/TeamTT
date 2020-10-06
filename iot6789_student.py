# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:43:12 2020

@author: balsw
"""

#sample player file which must be made by student

from player import *
from stone import *
from random import *

class iot6789_student(player):
    def _init_(self, clr):
        super()._init_(clr) #call constructor of super class, self 제거
        
        
    def _del_(self): #destructor
        pass
    
    def next(self, board, length): #override
        print("***Black Player: My Turns***")
        stn=stone(self._color) #protected variable
        while True:
            x=randint(0,length-1) % length
            y=randint(0,length-1) % length
            if(board[x][y]==0):
                break
            
        stn.setX(x)
        stn.setY(y)
        print("===Black Player was completed===")
        return stn