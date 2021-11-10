
import pandas as pd
from player import Player
from utility import Utility

class Game:
  
  def __init__(self, game_id, size, name1, name2, game_result=None):

    self.game_id = game_id

    #initialize the players and the game board
    self.player1 = Player(name1, 'x', 1)
    self.player2 = Player(name2, 'o', 0)

    #Use dataFrame to simulate the game board. Initialize all elements as 'null' 
    self.gameBoard = pd.DataFrame(index=range(self.size),columns=range(self.size))
    self.gameBoard.fillna('null')
     
  def update_game_result(self, player_name):  #game_result default value is None, i.e. a draw. If there is a winner, assign winner's name as it's value
    self.game_result = player_name

  def check_game_result(self):
    return self.game_result

  def check_gameBoard(self, df):
    
    row_sum = Utility().row_or_col_sum(df, axis_option=1) 
    col_sum = Utility().row_or_col_sum(df, axis_option=0)
    dia_sum = Utility().diagonal_sum(df)
    all = [row_sum, col_sum, dia_sum]

    for i in 

    

  def save_game_to_db(self):
    print("save the game to DB")

      
    
  

