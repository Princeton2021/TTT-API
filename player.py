from collection import defaultdict

class Player:

  def __init__(self, name, symbol):

    #symbol = 'x' or 'o' 

    self.player = name
    self.symbol = symbol
    
    #To record players' choice in each step in the game
    self.play_history = defaultdict(tuple)

    self.winner = None
    self.player_turn = None
    self.player_wait = None

  def set_winner(self, player_name):
    #winner is one of the players. If the game is a draw, set winner = None
    self.winner = player_name

  def add_play_history(self, symbol, number, step):
    #symbol: 'x' or 'o'. can stand for player
    #number: player's choice of the square in the game board
    self.play_history[step] = (symbol, number)

  def set_a_turn(self, player_name1, player_name2):
    #when one plays, the other has to wait
    self.player_turn = player_name1
    self.player_wait = player_name2
    