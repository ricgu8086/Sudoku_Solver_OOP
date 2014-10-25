# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 21:24:36 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""


import numpy as np
from matplotlib.mlab import find



class recursiveBacktracking(object):
    
    def __init__(self):
        self.solution = None
        
    def init(self,original):
        '''
        matrix: array_like
            It contains the initial sudoku matrix.
        '''
        
        self.original = original
        self.matbool = original != 0
        
        
        
    def prettyPrint(self, matrix):
        '''
        prettyPrint takes a sudoku contained in a numpy array and prints it 
        in a friendly way.
        
        Parameters
        ----------
        matrix: array_like
            It contains the sudoku matrix.
        '''
        
        rows, columns = matrix.shape
        
        line = ' ' + '+'.join(['-'*3]*3)
    
        
        for a in range(0,rows):
            if a and a%3 == 0:
                print line
                
            str_row = ''.join(str(val) for val in matrix[a,:])
            print ' ' + '|'.join(str_row[i:i+3] for i in range(0,len(str_row),3)),
    
            print '\n',
        
        print '\n'


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
        The algorithm implemented in this method is based on the recursive 
        backtracking algorithm described in [1].
    
        [1] http://es.wikipedia.org/wiki/Sudoku_backtracking
        '''
        
        self.solveRec(0,0)
        
        return self.solution



    def solveRec(self, i, j): 
        '''
        This is a helper recursive function used by solver.
        
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
       
       
    def checker(self, matrix):
        '''
        checker takes a 9x9 sudoku and return True if it is a valid sudoku,
        i.e. it meets all the rules.
        
        Parameters
        ----------   
        matrix: array_like
                `matrix` is a numpy.array that contains a 9x9 sudoku.
        
        Returns
        -------
        valid : bool
            If any of the numbers in `matrix` does not follow the 3 sudoku's rules, 
            `out` will be False. Otherwise will be True.
        '''
        
        valid = True
        
        if len( np.hstack((find(matrix <1), find(matrix > 9))) ) != 0:
            valid = False
            return valid
            
        for i in range(0,9):
            for j in range(0,9):
                
                k = matrix[i,j]
                
                if len(find(matrix[i,:] == k)) > 1 or \
                   len(find(matrix[:,j] == k)) > 1 or \
                   len(find(self.mySquare(i,j) == k)) > 1:
                       
                       valid = False
                       
            return valid
