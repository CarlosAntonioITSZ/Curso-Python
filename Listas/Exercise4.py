#Exercise4

'''
Design the algorithm corresponding to a program, which:

Create a table (list with two dimensions) of 5x5 integers.

Load the table with integer numerical values.

Add all the elements of each row and all the elements 
of each column displaying the results on the screen.
'''

#@CarlosAntonio

list=[[1,2,3,4,5],
      [1,2,3,4,5],
      [1,2,3,4,5],
      [1,2,3,4,5],
      [1,2,3,4,5]]

sumRow=0
sumColumn=0

for row in range(0,5):
    for column in range(0,5):
            sumRow+=list[row][column]
            sumColumn+=list[column][row]

print("")
print(list)
print("")
print(sumRow)
print(sumColumn)
