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
    prettyPrint : static method.
        prettyPrint takes a sudoku contained in a numpy array and prints it 
        in a friendly way.
    checker : static method.
        checker takes a 9x9 sudoku and return True if it is a valid sudoku,
        i.e. it meets all the rules.
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