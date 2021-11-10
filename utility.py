"""
Map numbers from 1 to nxn to nxn table cell (row,column) index (row,column). Use the (row, column) to access the game board DataFrame table

Example:

1,2,3,4,5,6,7,8,9 --> ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))

    |     |                   |       |
__1_|__2__|__3__        (0,0) | (0,1) | (0,2)
    |     |      --->   ---------------------
__4_|__5__|__6__        (1,0) | (1,1) | (1,2)
    |     |              ---------------------
  7 |  8  |  9          (2,0) | (2,1) | (2,2)
                              |       |
      
  
"""
from collection import defaultdict

def mapNumberToTableCellIndex(size):

  num_to_index = defaultdict(tuple)
  
  for i in range(size):
    for j in range(size):
      num = i*size+j
      num_to_index[num] = (i,j) 
       
  return num_to_index