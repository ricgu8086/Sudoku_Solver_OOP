# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 21:57:21 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""

import numpy as np
import sys
import os
from sudokuAlgFactory import sudokuAlgFactory
from sudokuCommonTools import sudokuCommonTools as suTools


def pause():
    '''
    This function pause the execution until the user press any key to continue
    \n(in Windows) or press Enter (in Linux)
    '''
    
    if sys.platform == 'win32':
        os.system('pause')
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        print('Press Enter to continue ...'),
        try:
            raw_input()
        except:
            pass
      
    print('\n')



if __name__ == "__main__":
    
    #Always parsing the user input
    #---------------------#
    
    if len(sys.argv) != 4:
        print('Invalid input. Usage: python sudokuSolver.py ALGORITHM_NAME '\
        'CSV_INPUT_PATH CSV_OUTPUT_PATH\n In this version only Backtracking '\
        'algorithm is implemented')
        pause()
        sys.exit(1)
    
    algorithm_name = sys.argv[1]
    csv_input_path = sys.argv[2]
    csv_output_path = sys.argv[3]
    
    
    try:
        matrix = np.loadtxt(csv_input_path, delimiter=',').astype('int');
        
    except IOError as e:
        print('There was an I/O error trying to read in path: ' + csv_input_path + \
        '.\nThe system returns: ' + e.strerror + '\nPlease check the path is correct\n')
        pause()
        sys.exit(1)
        
    except:
        print('There was an error trying to convert the file into an integer matrix.'\
        + '\nPlease check if there is any empty space between commas or any '\
        ' non-proper symbol.')
        pause()
        sys.exit(1)
    
    if matrix.shape != (9,9) or\
        matrix.min() < 0 or \
        matrix.max() > 9:
            
        print('Sorry, this sudoku solver only works with the standard sudoku version' \
        + ' of a 9x9 grid with values between 1 and 9, using 0 as a blank box')
        pause()
        sys.exit(1)
    
    #---------------------#
    
    
    algo = sudokuAlgFactory.create(algorithm_name)
    algo.setInitialGrid(matrix)
    
    print('\nThis is the given sudoku:\n\n')
    suTools.prettyPrint(algo.original)
    
    print('Please, wait while solving ...\n')
    solution = algo.solve()
        
    print('Solving process already done')
    pause()
    
    print('This is the solved sudoku:\n\n')
    suTools.prettyPrint(algo.solution)
    pause()
    
    print('Saving in ' + csv_output_path + ' ...\n')
    
    
    
    try:
        np.savetxt(csv_output_path, solution, fmt='%d', delimiter=',')
    except IOError as e:
        print('There was an IO error trying to write in path: ' + csv_output_path + \
        '\nThe system returns: ' + e.strerror)
        pause()
        sys.exit(1)
        
        
    print('Complete')
