Sudoku_Solver_OOP
=================

This is the object-oriented version of a sudoku solver I developed for the Insight Data Engineering Fellows Program.

This design uses the Factory Method pattern to allows interchange the algorithm without modifying the main program (sudokuSolver.py), thus reducing the coupling.

By now, there is only one algorithm supported and it's called *Backtracking*. It is based on the recursive backtracking algorithm described in [1].

In `sudokus_for_testing` directory there are sudokus of different complexity levels for testing the application.

Requirements
============

* NumPy.
  As described in their web "NumPy is the fundamental package for scientific computing with Python".
  
  It can be downloaded from [2].

* Matplotlib.

  It is described as "python 2D plotting library which produces publication quality figures in a variety of hardcopy    formats and interactive environments across platforms".
  
  It can be downloaded from [3].

An example of use:
==================
>~~~
>>>> python sudokuSolver.py Backtracking E:/sudokus_for_testing/fiendish.csv E:/sudokus_for_testing/sudokuOUT.csv
>
>This is the given sudoku:
>
>
> 006|504|800 
> 017|900|020 
> 900|030|065 
> ---+---+---
> 800|060|092 
> 003|709|600 
> 620|010|003 
> ---+---+---
> 180|050|007 
> 060|003|240 
> 002|807|100 
>
>
>Please, wait while solving ...
>
>Solving process already done
>Presione una tecla para continuar . . . 
>
>
>
>This is the solved sudoku:
>
>
> 236|574|819 
> 517|986|324 
> 948|231|765 
> ---+---+---
> 871|365|492 
> 453|729|681 
> 629|418|573 
> ---+---+---
> 184|652|937 
> 765|193|248 
> 392|847|156 
>
>
>Presione una tecla para continuar . . . 
>
>
>
>Saving in E:/sudokus_for_testing/sudokuOUT.csv ...
>
>Complete
>>>> 
>~~~

References
==========

[1] http://es.wikipedia.org/wiki/Sudoku_backtracking

[2] http://www.numpy.org/

[3] http://matplotlib.org/
