# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 00:20:59 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 23:53:45 2014

@author: Ricardo
"""

from recursiveBacktracking import recursiveBacktracking

class sudokuAlgFactory(object):
    '''
    The class sudokuAlgFactory implements the Factory Method pattern to deal
    with the instantiation of a concrete algorithm without exposing the
    instantiation logic to the main program, thus reducing the coupling
    
    Methods
    -------
    create: static method
        It returns an object that contains the selected algorithm for solving
        a sudoku.
    '''
    
    availableAlgorithms = {'Backtracking': recursiveBacktracking}
    
    @staticmethod
    def create(name):
        '''
        create is a static method that returns an object that contains the 
        selected algorithm for solving a sudoku.
        
        Parameters
        ----------
        
        name: str
            this is the name of the selected algorithm.
        '''
        
        return sudokuAlgFactory.availableAlgorithms[name]()
        
