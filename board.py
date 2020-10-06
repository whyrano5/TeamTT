# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:58:00 2020

@author: balsw
"""

from stone import *
from os import system, name

class board:
    def _init_(self, size=15):
        self._size=size
        self._game_board=[[0 for i in range(self._size)] for j in range(self._size)]
    def _del_(self): #소멸자
    #print("board instance is destroyed")
        pass

    def update(self, st):
        x = st.getX()
        y = st.getY()
        stone = st.getStone()
        print(x,",", y,":", stone)
        self._game_board[x][y]=stone
        self.display()
    def show(self):
        return self._game_board
    def get(self,x,y):
        return self._game_board[x][y]
    def display(self):
        #for windows
        if name == 'nt':
            _=system('cls')
        #for mac and linux(here, os.name is 'posix')
        else:
            _=system('clear')
            print("{0:^3}".format(" "), end="") #no newline
            for i in range(0, self._size):
                print("{0:^3}".format(i), end="") #no newline
            print() #new line
            for i in range(self._size-1,-1,-1):
                print("{0:^3}".format(i), end="") #no newline
                for j in range(0, self._size):
                    val=self.write_char(self._game_board[i][j]) #no newline
                    print("{0:^3}".format(val),end="") #no newline
                print() #new line
    def write_char(self,stn):
        if(stn==1):
            return 'W'
        elif(stn==-1):
            return 'B'
        elif(stn==0):
            return '.' # '+'
        else:
            return '.' # '+'
            