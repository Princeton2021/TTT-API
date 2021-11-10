
from gameBoard import GameBoard
from player import Player

player1 = Player(name1, 'x', 1)
player2 = Player(name2, 'o', 0)

gameBoard = GameBoard(size)
gameBoard.printGB()



class Game:
  
  def __init__(self, game_id, size, name1, name2, result, game_history):
    
    self.game_id = game_id
    self.player1 = player1
    self.player2 = player2
    self.result = None
    

  def update(self, name):
    self.result = name

  def save_to_db(self):
    print("save the game to DB")

  def create_db(self):
    print("create db")
    

    

    
    
  

