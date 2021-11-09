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


