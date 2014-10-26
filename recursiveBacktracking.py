# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 21:24:36 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""

import numpy as np
from matplotlib.mlab import find


class recursiveBacktracking(object):
    ''' 
    The algorithm implemented in this class is based on the recursive 
    backtracking algorithm described in [1].

    [1] http://es.wikipedia.org/wiki/Sudoku_backtracking
    '''
    
    def __init__(self):
        '''
        Dummy constructor. It takes no parameters. The real initialization
        is done when the method `setInitialGrid` is called.
        '''
        
        self.solution = None
        self.original = None
        self.matbool = None
        
    def setInitialGrid(self,original):
        '''
        This method sets the initial sudoku that will be used within the class.
        
        Parameters
        ----------        
        matrix: array_like
            It contains the initial sudoku matrix.
        '''
        
        self.original = original
        self.matbool = original != 0

    def mySquare(self, a, b):
        '''
        This method returns the square to which the variable in coordinates 
        a,b belongs.
        
        Parameters
        ----------
        a : int
            Current row.
        b : int
            Current column.
            
        Returns
        -------
        squares : array_like
            Returns a sub array from `squares` that contains the 3x3 square
            to which belongs the element located in `original`[`a`,`b`]
        '''    
        
        #Converting full grid to collection of 3x3 squares
        squares = np.swapaxes(self.original.reshape(3,3,3,-1),1,2)    
        
        #mapping indexes a,b in original to c,d in squares
        equiv = {0: [0,1,2], 1: [3,4,5], 2: [6,7,8]}
        c = [key for key in equiv if a in equiv[key]][0]
        d = [key for key in equiv if b in equiv[key]][0]
        
        return squares[c,d]
    

    def solve(self):
        '''
        solve method implements Recursive Backtracking. 
        It initializes the recursive function that takes care of the
        whole algorithm
        
        Parameters
        ----------
        solution: array_like
            Retuns a numpy array of 9x9 that contains the solution of the
            initial sudoku given in `setInitialGrid`
        '''
        
        self.solveRec(0,0)
        
        return self.solution



    def solveRec(self, i, j): 
        '''
        This is a helper recursive function used by solver.
        It stores the solved sudoku in `self.solution`
        
        Parameters
        ----------
        i : int
            Current row.
        j : int
            Current column.
        '''
        
        if self.matbool[i,j] == False:
            
            for k in range(1,10):
                
                self.original[i,j] = k
                
                #checking if value is plausible in row, col and square
                if len(find(self.original[i,:] == k)) == 1 and \
                   len(find(self.original[:,j] == k)) == 1 and \
                   len(find(self.mySquare(i,j) == k)) == 1:              
                   
                   if i == 8 and j == 8:
                       self.solution = self.original.copy()
                   elif i < 8 and j == 8:
                       self.solveRec(i+1, 0)
                   else:
                       self.solveRec(i, j+1)
                    
                self.original[i,j] = 0       
        else:
            
            if i == 8 and j == 8:
                self.solution = self.original.copy()
            elif i < 8 and j == 8:
                self.solveRec(i+1, 0)
            else:
                self.solveRec(i, j+1)    
       
       