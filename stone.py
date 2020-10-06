# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:07:36 2020

@author: balsw
"""

from board import *

class stone:
    def _init_(self):
        self._size=15 #private
        self._x = 7
        self._y = 7
        self._bw=0 #black or white or none
        
    def _init_(self,stn,sz=15):
        self._size=sz #private : variable with double underscore
        self._x=(self._size-1)//2 #integer division
        self._y=(self.size-1)//2 #integer division
        self._bw=stn
        
    def _del_(self): #소멸자
        #print("stone 객체가 소멸합니다.")
        pass
    
    def set(self,posX,posY,stn):
        self._x = posX % self._size
        self._y = posX % self._size
        self._bw = stn
        
    def setStone(self,stn):
        self._bw=stn
        
    def setX(self,posX):
        self._x = posX % self._size
        
    def get(self):
        ret=stone()
        ret.set(self._x,self._y,self._bw)
        return ret
    
    def getStone(self):
        return self._bw
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y