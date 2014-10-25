# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 00:20:59 2014

@author: Ricardo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 23:53:45 2014

@author: Ricardo
"""

from sudokuClass import recursiveBacktracking

class sudokuAlgorithms(object):
    
    availableAlgorithms = {'Backtracking': recursiveBacktracking}
    
    @staticmethod
    def create(string):
        return sudokuAlgorithms.availableAlgorithms[string]
        
