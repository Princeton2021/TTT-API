import pandas as pd
import logging
from collections import defaultdict

"""
mapNumberToTableCellIndex(size):

Map numbers from 1 to nxn to nxn table cell (row,column). Use the (row, column) to access the game board DataFrame table

Example:
n = 3, nxn = 9

  1,2,3,4,5,6,7,8,9 --> ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))

    |     |                   |       |
__1_|__2__|__3__        (0,0) | (0,1) | (0,2)
    |     |      --->   ---------------------
__4_|__5__|__6__        (1,0) | (1,1) | (1,2)
    |     |              ---------------------
  7 |  8  |  9          (2,0) | (2,1) | (2,2)
                              |       |
      
The DataFrame table can be used to simulate the gameboard. The value of each cell is either 0,1 or null. By calulating the sum of the non-null values in row, col, and diagnal, the winner can be determined.

"""

class Utility:

  #Create and configure logger
  logging.basicConfig(filename="newfile.log",
    format='%(asctime)s %(message)s',filemode='w')
  
  #Creating an object
  logger=logging.getLogger() 
  logger.info("Just an information")

  def mapNumberToTableCellIndex(self,size):

    num_to_index = defaultdict(tuple)
  
    for i in range(size):
      for j in range(size):
        num = i*size+j
        num_to_index[num] = (i,j) 
       
    return num_to_index

  #The following methods are for DataFrame calculation, i.e. for game board

  #update dataFrame cell
  def update(self,row, col, value, df):
    df.iat[row, col] = value
    return df

  #Check value in the dataFrame cell, 
  def check(self, row, col, df):
    if pd.isna(df.iloc[col,row]):
      return None
    else:
      return df.iat[row,col]

  #calculate the sum of row or col in the dataFrame 
  def row_or_col_sum(self,df, axis_option):  #axis_option: 1 for row, 0 for column 
    # Select rows(columns) which do not contain any null values in all columns(rows)
    selected = df[~df.isnull().any(axis=axis_option)]
    sum = selected.sum(axis=axis_option)
    return sum.tolist()

  #calculate the sum of the diagonal in the dataFrame
  def diagonal_sum(self,df): 
    sum_of_diagonal = 0
    for i in range(len(df)):
      if pd.isna(df.iloc[i,i]):
        return None
      sum_of_diagonal += df.iat[i, i]
    return sum_of_diagonal

