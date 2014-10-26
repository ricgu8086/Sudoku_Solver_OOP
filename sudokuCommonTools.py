# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 00:50:59 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""

import numpy as np
from matplotlib.mlab import find

class sudokuCommonTools(object):
    '''
    This class implements a bunch of useful static methods to deal with sudokus.
    
    Methods
    -------
    prettyPrint : static method
        prettyPrint takes a sudoku contained in a numpy array and prints it 
        in a friendly way.
    checker : static method
        checker takes a 9x9 sudoku and return True if it is a valid sudoku,
        i.e. it meets all the rules.
    inputChecker: static method
        inputChecker takes a sudoku and return True if it is a valid initial
        sudoku, i.e. it's shape is 9x9 and it meets all the rules for non-zero values.
    mySquare: static method
        is a helper function used by checker and inputChecker. Given 2 coordinates
        it returns a 3x3 subarray to which belongs the element in those coordinates.
    ''' 
    
    @staticmethod
    def prettyPrint(matrix):
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
    
    
    @staticmethod
    def checker(matrix):
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
            
        for i in range(0,9):
            for j in range(0,9):
                
                k = matrix[i,j]
                
                if len(find(matrix[i,:] == k)) > 1 or \
                   len(find(matrix[:,j] == k)) > 1 or \
                   len(find(sudokuCommonTools.mySquare(i,j) == k)) > 1:
                       
                       valid = False
                       
            return valid
          
          
    @staticmethod
    def inputChecker(matrix):
        '''
        inputChecker takes a sudoku and return True if it is a valid initial
        sudoku, i.e. it's shape is 9x9 and it meets all the rules for non-zero values.
        
        Parameters
        ----------   
        matrix: array_like
                `matrix` is a numpy.array that contains a 9x9 sudoku.
                
        Returns
        -------
        valid : bool
            If the input matrix is correct, a True value will be returned.
        '''
        
        valid = True
        
        if matrix.shape != (9,9) or\
            matrix.min() < 0 or \
            matrix.max() > 9:
                
            valid = False
            return valid
            
        for i in range(0,9):
            for j in range(0,9):
                
                k = matrix[i,j]
                
                if k != 0:
                    if len(find(matrix[i,:] == k)) > 1 or \
                       len(find(matrix[:,j] == k)) > 1 or \
                       len(find(sudokuCommonTools.mySquare(matrix,i,j) == k)) > 1:
                           
                           valid = False
                       
            return valid
  
        
    @staticmethod
    def mySquare(matrix, a, b):
        '''
        This method returns the square to which the variable in coordinates 
        a,b belongs.
        
        Parameters
        ----------
        matrix: array_like
            `matrix` is a numpy.array that contains a 9x9 sudoku.
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
        squares = np.swapaxes(matrix.reshape(3,3,3,-1),1,2)    
        
        #mapping indexes a,b in original to c,d in squares
        equiv = {0: [0,1,2], 1: [3,4,5], 2: [6,7,8]}
        c = [key for key in equiv if a in equiv[key]][0]
        d = [key for key in equiv if b in equiv[key]][0]
        
        return squares[c,d]