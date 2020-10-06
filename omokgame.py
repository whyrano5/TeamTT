# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:18:20 2020

@author: balsw
"""

from board import *
#from player import *
from iot6789_student import *
from stone import *
from iot12345_student import *
from iot6789_student import *

class omokgame:
    def _init_(self, sz):
        self._size=sz
        self._bd = board(self._size)
        #self._black = player(-1)
        self._black = iot6789_student(-1)
        self.white = iot12345_student(1)
        self._turns = 0
        self._next = -1
        self._draw = 0
        self._winner = 0
        self._bd.display()
    def _del_(self):
        #print("omok instanced is destroyed")
        pass
    def game_start(self):
        #do ~ while
        while True:
            self._Truns += 1 #increment
            self.msg_display()
            
            if(self._next == -1):
                print("black Player: Turns = %5d" % self._turns)
                time = 0
                # do while
                while True:
                    print("black Player: time = %5d" % time)
                    stn_b = self._black.next(self._bd.show(), self._size)
                    time += 1
                    if((time >= 4) or (self.validCheck(stn_b))):
                        break
                if(time < 4):
                    self._bd.update(stn_b)
                else:
                    print("Too many wrong input, black's turn is over")
                self._next = self._next * (-1)
            elif(self._next == 1):
                print("black Player: Turns = %5d" % self._turns)
                time = 0
                #do while
                while True:
                    print("white Player: time = %5d" % time)
                    time += 1
                    if((time >= 4) or (self.validCheck(stn_w))):
                        break
                if(time < 4):
                    self._bd.update(stn_w)
                else:
                    print("Too many wrong input, white's turn is over")
                self._next = self._next * (-1)
            if(self.endCheck()): #do-while end
                break
        self._winner = self._next * (-1)
        self.msg_display()
    
    def msg_display(self):
        if(self._turns != 0 and self._winner == 0):
            print("Turn ", self._turns, ",", end = "")
            if(self._next == -1):
                print("Black")
            elif(self._next == 1):
                print("White")
        if(self._draw ==1):
            print()
            print("== No Winner: Game Result is draw")
        elif(self._winner != 0):
            print()
            print("Congraturation!")
            print("The winner is ", end="")
            if(self._winner == -1):
                print("Black!!")
            elif(self._winner == 1):
                print("White!!")
                
                
    def endCheck(self):
        #horizontal omok
        for i in range(0, self._size):
            for j in range(0, self._size-4):
                if(self._bd.get(i,j)!=0):
                    check=self._bd.get(i,j)+self._bd.get(i,j+1)+self._bd.get(i,j+3)+self._bd.get(i,j+4)
                    if(check == 5 * self._bd.get(i,j)):
                        return True
        #vertical omok
        for i in range(0, self._size):
            for j in range(0, self._size-4):
                if(self._bd.get(j,i)!=0):
                    check=self._bd.get(j,i)+self.bd.get(j+1,i)+self._bd.get(j+3,i)+self._bd.get(j+4,i)
        #diagonal 1
        for i in range(0, self._size-4):
            for j in range(0, self._size-4):
                if(self._bd.get(i,j)!=0):
                    check=self._bd.get(i,j)+self._bd.get(i+1,j+1)+self._bd.get(i+2,j+2)+self._bd.get(i+3,j+3)+self._bd.get(i+4,j+4)
                    if(check == 5 * self._bd.get(i,j)):
                        return True
        #diagonal 2
        for i in range(0, self._size-4):
            for j in range(4, self._size):
                if(self._bd.get(i,j)!=0):
                    check=self._bd.get(i,j)+self._bd.get(i+1,j-1)+self._bd.get(i+2,j-2)+self._bd.get(i+3,j-3)+self._bd.get(i+4,j-4)
                    if(check == 5 * self._bd.get(i,j)):
                        return True
        #draw check : turns >= max
        if(self.drawCheck()):
            return True
        #no match (no Omok)
        
        return False
    
    def drawCheck(self):
        if(self._turns >= self._size * self._size -2):
            self._draw = 1
            return True
        else:
            self._draw = 0
            return False
        
    def validCheck(self,stn):
        #3 by 3 check => not implemented
        #overlapped check
        if(self._bd.get(stn.getX(), stn.getY())!= 0):
            return False
        return True
    
                    