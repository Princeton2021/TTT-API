
from gameBoard import GameBoard
from player import Player

class Game:
  
  def __init__(self, game_id, size, name1, name2, result=None, game_history=[]):

    #initialize the players and the game board
    self.game_id = game_id
    self.player1 = Player(name1, 'x', 1)
    self.player2 = Player(name2, 'o', 0)
    self.game_board = GameBoard(size)
    
  def update(self, name):
    self.result = name

  def save_to_db(self):
    print("save the game to DB")

  def create_db(self):
    print("create db")
    

    

    
    
  

