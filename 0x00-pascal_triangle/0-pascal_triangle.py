#!/usr/bin/python3

"""pascal's triangle"""

def pascal_triangle(n):

    """this module returns a list of lists of integers representing pascal's triangle
   
   Raise:
       TypeError: if the input n is not an integer
       """
if not isinstance(n, int):
    raise TypeError("input mast be an integer")

if type(n) is not int or n <= 0:
    return pascal
       
pascal = [[] for idx in range(n)]
       
for row in range(n):
    for col in range(row + 1):
        if (col < row):
            if (col == 0):
                pascal[row].append(1)
            else:
                pascal[row].append(pascal[row-1][col] + pascal[row-1][col-1]
        
                        elif(col == row):
                        pascal[row].append(1)
return pascal
