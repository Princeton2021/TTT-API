"""
Map numbers from 1 to nxn to nxn table cell (row,column) index (row,column). Use the (row, column) to access the game board DataFrame table
"""
from collection import defaultdict

def mapNumberToTableCellIndex(size):

  num_to_index = defaultdict(tuple)
  
  for i in range(size):
    for j in range(size):
      num = i*size+j
      num_to_index[num] = (i,j) 
       
  return num_to_index