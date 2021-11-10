import pandas as pd
from player import Player
from utility import Utility
import logging

#Create and configure logger
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
#Creating an object
logger=logging.getLogger() 
logger.info("For review")

class Game:
  
  def __init__(self, game_id, size, name1, name2, game_result=None):

    self.game_id = game_id

    #initialize the players and the game board
    self.player1 = Player(name1, 'x', 1)
    self.player2 = Player(name2, 'o', 0)
    self.size = size

    #Use dataFrame to simulate the game board. Initialize all elements as 'null' 
    self.gameBoard = pd.DataFrame(index=range(self.size),columns=range(self.size))
    self.gameBoard.fillna('null')
     
  def update_game_result(self, player_name):  #game_result default value is None, i.e. a draw. If there is a winner, assign winner's name as it's value
    self.game_result = player_name

  def check_game_result(self):
    return self.game_result

  def check_gameBoard(self, df):
    #calculate sum in row, col, and dial 
    row_sum = Utility().row_or_col_sum(df, axis_option=1) 
    col_sum = Utility().row_or_col_sum(df, axis_option=0)
    dia_sum = Utility().diagonal_sum(df)
    
    #combine them together to check
    all = [row_sum, col_sum, dia_sum]

    #sums can not have 0 and 1*size coexist, i.e. the game cannot have 2 winners. If so, the code has errors. Need to check

    if 0 in all and self.size in all:
      logger.errors(all+" the results are incorrect")
      return "Need to check the code"

    #If there is 0 or 1*size in the list, there is a winner. return the winner associate with the value
    if 0 in all:
      #the winner is player 2
      return self.player2
    
      #the winner is player 1
    if self.size in all:
      return self.player1

    #return "None" if there is no winner
    return 'None'
    
  def save_game_to_db(self):
    print("save the game to DB")
