# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:31:40 2019

@author: Tanay's PC
"""
# The main function
def sudokuCheck(grid):
    
#Rules for validation
    if len(grid) < 1:
        return False
    for i in grid:
       if len(i) != len(grid):
           return False
    if (len(grid)** 0.5) == False:
        return False
    
# Function to check for duplicates  
    def dup(x):
        for i in range(len(x)):
            if x[i] in x[i+1:]:
                return True
        return False
    
    
    for row in grid:
        if dup(row):
            return False
    
    for col in range(len(grid)):
        column = []
        for row in range(len(grid)):
            val = grid[row][col]
            column.append(val)
        if dup(column):
            return False

# Function to check individual 'boxes'
    def boxCheck(grid):
        boxSize = int(len(grid)**0.5)
        for i in range(boxSize, (boxSize**2)+1, boxSize):
            for ii in range(boxSize, (boxSize**2)+1, boxSize):
                box = []
                for rows in grid [i-boxSize:i]:
                    box.extend(rows[ii-boxSize:ii])
                if dup(box):
                    return False
    
    boxCheck(grid)
    return "Good Sudoku!"


simple = [[1,2,3,4],
          [2,3,4,1],
          [3,4,1,2],
          [4,1,2,3]]

ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

wrong = [[2,9,0,0,0,0,0,7,0],
       [3,0,6,0,0,8,4,0,0],
       [8,0,0,0,4,0,0,0,2],
       [0,2,0,0,3,1,0,0,7],
       [0,0,0,0,8,0,0,0,0],
       [1,0,0,9,5,0,0,6,0],
       [7,0,0,0,9,0,0,0,1],
       [0,0,1,2,0,0,3,0,6],
       [0,3,0,0,0,0,0,5,9]]

valid = [[8, 1, 2, 7, 5, 3, 6, 4, 9],
         [9, 4, 3, 6, 8, 2, 1, 7, 5],
         [6, 7, 5, 4, 9, 1, 2, 8, 3],
         [1, 5, 4, 2, 3, 7, 8, 9, 6],
         [3, 6, 9, 8, 4, 5, 7, 2, 1],
         [2, 8, 7, 1, 6, 9, 5, 3, 4],
         [5, 2, 1, 9, 7, 4, 3, 6, 8],
         [4, 3, 8, 5, 2, 6, 9, 1, 7],
         [7, 9, 6, 3, 1, 8, 4, 5, 2]]


print(sudokuCheck(simple))
print(sudokuCheck(ill_formed))
print(sudokuCheck(wrong))
print(sudokuCheck(valid))


        