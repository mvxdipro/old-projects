# Minesweeper Game - playable with ripple implementation
# Author: Mahdi Mohamed
#username: Mohamedm2    

import random
from graphics import *
import sys

class MineSweeper():
    """ This class implements the Minesweeper game found on Windows OS
    It contains 2 grids, one for the player view and one for the hidden values
    of each cell, where both are implemented as lists of lists. """
    
    def __init__(self, size, win):
        """ constructor for MineSweeper class, takes in grid size (always square),
        and GraphWin object to draw things to later.  Also initializes hidden
        values and player view grids """
        
        self.size = size
        self.win = win

        # hidden grid initialized to all 0's as have not placed mines yet
        self.hidden=[]  
        for i in range(self.size):
            self.hidden.append([0]*self.size)
            
        # player view grid initialized to all 'c' for "closed" cell
        self.pview = []
        for i in range(self.size):
            self.pview.append(['c']*self.size)

    
    def printInstructions(self):
        """ prints instructions for Minesweeper before game begins """
        print("Click on a square to uncover that cell in the grid.")
        print("If the cell was a mine you lose and the entire board will be shown.")
        print("Otherwise the now open cell will display the number of mines")
        print("that surround the opened cell in all adjacent cells on the grid,")
        print("including those diagonal to the opened cell.")
        print("Open all non-mine cells without clicking any mines to win!")


    
    def printBoard(self):
        """ method to print playerview of Minesweeper grid.  Blank white rectangle
        for still covered cells, or the actual value from the hidden grid for cells
        that have been selected and opened """
        
        for i in range(self.size):
            for j in range(self.size):
                # translate grid coordinates to actual pixels on screen to
                # draw rectangle around current cell. Place text in middle of cell
                # rectangle if this cell is not still closed.
                # Note - each cell in the grid is 20x20 pixels, and the entire grid
                # is offset by 100 pixels from the edge of the window
                r = Rectangle( Point(100+i*20,100+j*20),
                               Point(100+i*20+20,100+j*20+20) )
                t = Text(Point(100+i*20+10,100+j*20+10), str(self.pview[i][j]))
                if not self.pview[i][j]=='c':
                    t.draw(self.win)
                r.draw(self.win)

   
    def printHiddenBoard(self):
        """ method to print hidden values of grid with mines and numbers """
        for i in range(self.size):
            for j in range(self.size):
                # translate grid coordinates to actual pixels on screen 
                r = Rectangle( Point(100+i*20,100+j*20),
                               Point(100+i*20+20,100+j*20+20) )
                t = Text(Point(100+i*20+10,100+j*20+10), str(self.hidden[i][j]))
                t.draw(self.win)
                r.draw(self.win)
                
    
    def placeMinesOnBoard(self, n):
        """ method called once on startup to randomly place n mines on the grid
        NOTE - uses lazy method of simply trying again with a new random num
               anytime attempt to place mine in cell that already has a mine.
               This can be slow if the ratio of mines to cells is high! """

        # sanity check to see if enough cells to place requested num mines
        if n > self.size*self.size:
            print("\n***ERROR!***")
            print("Cannot place more mines than there are cells in the grid!\n")
            quit()

        numMines = 0
        while numMines < n:
            # only need 1 random number between 0 and total num cells on grid
            # treat grid as 1 long list of cells and translate that random num
            # to the actual grid coordinates accordingly
            r = random.randrange(0,self.size*self.size)
            x = r//self.size
            y = r%self.size

            # if we happened to pick a cell that already has a mine, don't
            # increment # mines placed so that will try to place this one again
            if self.hidden[x][y]!="M":
                self.hidden[x][y]="M"
                numMines+=1

    
    def isWon(self):
        """ returns True if game is won (all non-mine cells uncovered),
        False otherwise """
        for i in range(self.size):
            for j in range(self.size):
                # if any mine is still covered, have not won yet
                if self.pview[i][j]=='c' and self.hidden[i][j]!='M':
                    return False
        return True
    
    
    def mineCountAtEachCell(self):
        """ sets correct mine count at each cell in hidden grid as
        total num mines in 8 adjacent cells (includes diagonals) """
        for i in range(self.size):
            for j in range(self.size):
                # only set count if this cell does not contain a mine itself
                if self.hidden[i][j]!='M':
                    tot = 0
                    for k in range(i-1,i+2):
                        for l in range(j-1,j+2):
                            # check that this adjacent cell is still in grid
                            if 0<=k<self.size and 0<=l<self.size:
                                if self.hidden[k][l]=='M':
                                    tot += 1
                    self.hidden[i][j]=tot
                           
                                     
    def openCell(self,x,y):
        """ handle user mouse input. x,y are coordinates of point user clicked, in
        terms of screen pixels. Open corresponding cell in grid, if found mine
        return False for game over. Else open cell and return True, except if
        cell contains a 0, call ripple function first. """

        # translate coordinates of click on screen to coordinates of cell in grid
        x = (x-100)//20
        y = (y-100)//20
        if self.hidden[x][y]=='M':
            return False
        else:
            # open cell to show user num mines, ripple if num=0
            self.pview[x][y] = self.hidden[x][y]
            if self.hidden[x][y]==0:
                self.ripple(x,y)
            return True

        
    def ripple(self, x, y):
    # only looks at the squares around it and keeps if from going out of range
        for ver in (int(y-1), y,int(y+1)): 
            for hor in (int(x-1),x, int(x+1)):
                if ver>=0 and ver< int(self.size):
                    if hor>=0 and hor< int(self.size):
                    # opens  closed cells
                        if  self.pview[hor][ver]=='c':
                            self.pview[hor][ver] = self.hidden[hor][ver]
                            if self.pview[hor][ver]==0:
                                # repeats opening closed cells 
                                self.ripple(hor,ver)

                            
                
                                





    
def main():
    """ main function creates game and runs through one play
    requires command line arguments for grid size (one dimension only as
    grid will always be square) and number of mines to place in the grid """

    if len(sys.argv) < 3:
        print("\nERROR - must include 2 command line arguments:\n  \
        1. grid size (grid will be square size x size) and\n  \
        2. number of mines to place in the grid!\n")
        quit()

    # initial game setup creates board with mines placed randomly and fills in
    # counts for each cell (all hidden of course to start)
    win = GraphWin("Minesweeper", 400, 400)
    game = MineSweeper(int(sys.argv[1]), win)
    game.placeMinesOnBoard(int(sys.argv[2]))
    game.mineCountAtEachCell()
    game.printBoard()

    # get mouse clicks from player to open cells until game won or lost
    winner = False
    while not winner:

        # pauses program until receives mouse click input from user, works same
        # way as input("...") function, except for mouse instead of keyboard
        # p will get set to the pixel coordinates on the screen where the mouse
        # was clicked
        p = win.getMouse()

        # openCell returns false if clicked cell had a mine, this means player
        # loses game, print hidden board to show where all mines were and quit loop
        if not game.openCell(p.getX(), p.getY()):
            print ("You Lose!")
            game.printHiddenBoard()
            break

        # print updated user board with newly opened cell, check if won
        game.printBoard()
        if game.isWon():
            winner = True
            
    if winner:
        print ("You won!  Congrats!")

    input("enter to quit")

main()
