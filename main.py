
import numpy as np
import pandas as pd
import logging
from utility import Utility
  
#Create and configure logger
logging.basicConfig(filename="newfile.log",
  format='%(asctime)s %(message)s',filemode='w')
  
#Creating an object
logger=logging.getLogger() 
logger.info("Just an information")

"""
#update dataFrame cell
def update(row, col, value, df):
  df.iat[row, col] = value
  return df

#Check value in the dataFrame cell
def check(row, col, df):
  if pd.isna(df.iloc[col,row]):
    return None
  else:
    return df.iat[row,col]

#calculate the sum of row or col in the dataFrame       
def row_or_col_sum(df, axis_option):  #axis_option: 1 for row, 0 for column 

  # Select rows(columns) which do not contain any null values in all columns(rows)
  selected = df[~df.isnull().any(axis=axis_option)]
  #selected = df[df.isnull().any(axis=axis_option)]
  #logger.info("Just an information")
  sum = selected.sum(axis=axis_option)
  return sum.tolist()

#calculate the sum of the diagonal in the dataFrame
def diagonal_sum(df): 
  sum_of_diagonal = 0
  for i in range(len(df)):
    if pd.isna(df.iloc[i,i]):
      return None
    sum_of_diagonal += df.iat[i, i]
  return sum_of_diagonal
"""
size = 9
def test():
  return "The selected number cannot exceed:",  size

print(test())

vec = np.arange(1, 10)
df = pd.DataFrame(vec.reshape(3, 3))
print(df)
ut=Utility()

sum=ut.row_or_col_sum(df, 1)
print(sum)

sum=ut.row_or_col_sum(df, 0)
print(sum)

sum=ut.diagonal_sum(df)
print(sum)

newdf =ut.update(1, 1, 'NULL', df)
print(newdf)

#sum=row_or_col_sum(newdf, 1)
#print(sum)

sum=ut.row_or_col_sum(newdf, 0)
print(sum)

check=ut.check(1, 1, newdf)
print("check=", check)








"""
from gameBoard import GameBoard
from player import Player

name1="clu"
name2="clu1"
size=3

player1 = Player(name1, 'x', 1)
player2 = Player(name2, 'o', 0)

gameBoard = GameBoard(size)
gameBoard.printGB()

take_turn = 0

#while gameBoard.checkAllElements():

if take_turn == 0: # it is the player1s take_turn

  input(name1+" Please enter your choice of move")

"""


