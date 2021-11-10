from collection import defaultdict

class Player:

  def __init__(self, name, symbol, value ):

    #symbol = 'x' or 'o' 
    #value = 1 or 0  #to fill in the square in the game board
    
    self.player = name
    self.symbol = symbol
    self.value = value

    #To record players' choice in each step in the game
    self.play_history = defaultdict(tuple)

  def set_winner(self, name):
    #winner is one of the players. If the game is a draw, set winner = None
    self.winner = name

  def add_play_history(self, symbol, number, step):
    #symbol: 'x' or 'o'. can stand for player
    #number: player's choice of the square in the game board
    self.play_history[step] = (symbol, number)

    



  

  