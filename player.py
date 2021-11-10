class Player:

  def __init__(self, name, symbol, value ):

    #symbol = 'x' or 'o'
    #value = 1 or 0

    self.player = name
    self.symbol = symbol
    self.value = value

  def set_winner(self, name):
    
    #winner is one of the players. If it is a draw, set winner = None
    self.winner = name




  

  