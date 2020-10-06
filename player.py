# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:15:06 2020

@author: balsw
"""

from stone import *

class player:
    def _init_(self, clr):
        self._color = clr #protected variable with single underscore
        
    def _def_(self):
        pass
    
    def next(self, board, length):
        print("****Black Player: My Turns****")
        stn=stone(self._color,length)
        pos=int(input("Input position x for new stone: "))
        while((pos<0) or (pos >= length)):
            pos=input("Wrong position, please input again: ")
            
        stn.setX(pos)
        pos=int(input("Input position y for new stone: "))
        while((pos<0) or (pos >= length)):
            pos=input("Wrong position, please input again: ")
            
        stn.setY(pos)
        print("===Black Player was completed===")
        return stn