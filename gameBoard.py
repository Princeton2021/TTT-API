import pandas as pd

class GameBoard:
    
    def __init__(self, size):

      #Game size is size x size. size > 2. 
      self.size = size 
      
      #Use dataFrame to model the game board. Initialize all elements as null 
      self.boardElements = pd.DataFrame(index=range(self.size),columns=range(self.size))
      self.boardElements.fillna('null')


    def printGB(self):
      print(self.boardElements)

    #If a player makes a valid selection, the game board will update the value in the corresponing cell
    def update(self, row, col, value):
      self.boardElements.iat[row, col] = value


    #Check if the player's selection is valid or not
    def check(self, row, col):
      if self.boardElements.iat[row,col].isnull():
        return None
      else:
        return self.boardElements.iat[row,col]
    
    
    def row_or_col_sum(self, axis_option):

      #calculate the sum of row or col in the gameBoard

      # Select rows which do not contain any null value in all columns
      selected_rows = self.boardElements[~self.boaddElements.isnull().any(axis=1)]
      print("selected_rows=", type(selected_rows))
      print(selected_rows)  
      sum_rows = selected_rows.sum(axis=1)
      print("type(sum_rows)",  type(sum_rows))
      for i in sum_rows:
        print(i)

       # Select columns which do not contain any null value in all rows
      selected_cols = self.boardElements[~self.boardElements.isnull().any(axis=0)]
      print("selected_cols=", type(selected_cols))
      print(selected_cols)  
      sum_cols = selected_cols.sum(axis=0)
      print("type(sum_cols)",  type(sum_cols))
      for i in range(sum_rows):
        print()


    def diagonal_sum(self):
      #calculate the sum of the diagonal in the gameBoard
      sum_of_diagonal = 0
      for i in range(self.size):
        if self.boardElements.iat[i, i].isnull():
          return None
        sum_of_diagonal += self.boardElements.iat[i, i]

      return sum_of_diagonal
