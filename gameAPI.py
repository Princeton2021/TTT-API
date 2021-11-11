#Rest API for Tic Tac Toe

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, marshal_with, fields, abort

from utility import Utility
import logging

#Create and configure logger
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
  
#Creating an object
logger=logging.getLogger() 
logger.info("For review")

import json
from game import Game

app = Flask(__name__)
api = Api(app)

#games information should come from DB. To be implemented
games={ {'game_id': "1", 'player1':  "Chi", 'player2': "Joanna"},
        {'game_id': "2", 'player1': "Bing", 'player2': "Jing" },
        {'game_id': "3", 'player1': "Andrew", 'player2': "Mark"}
}

def abort_if_exist(game_id):
  if game_id in games:
        abort(409, message="A game with this id alreaady exist")

def abort_if_not_exist(game_id):
    if game_id not in games:
        abort(404, message="A game with this id does not exist")

#Base URL
@app.route("/")
def index():
  return "Welcome to Tic Tac Toa API"

#GET /api/games: Return a list of the Games known to the server, as JSON.
@app.route("/api/games", methods=['GET'])
def get_games():
  return jsonify({'games':games})

#GET /api/games/<id>: Retrieve a Game by its ID, returning a 404 status code if no game with that ID exists.
@app.route("/api/games/<int:game_id>", methods=['GET'])
def get_a_game(game_id):
  abort_if_not_exist(game_id)
  return jsonify({'games':games[game_id]})

#POST /api/games: Create a new Game, assigning it an ID and returning the newly created Game.
@app.route("/api/games", methods=['POST'])
def create_a_game():

  """
  Two way to assign an id to a new game
  #1. Randomly generate a game_id, and make sure the id has not been used
  #2. Always create the game_id by incrementing the length of games by 1. Use #2 here

  """
  game_id = len(games)+1

  #do POST with curl or in postman to send the request to the server
  #use the players information from the POST to create a new game
  new_data = request.json

  #get the players name from the POST data
  name1 = new_data.get['player1']
  name2 = new_data.get['player2']

  #create a new game
  result = None 
  new = Game(game_id, name1, name2, result)
  logger.info("created a new game: "+new)

  #add and commit the new game to the DB. To be implemented
  game={'game_id': game_id, 'player1': name1, 'player2': name2}
  
  games[game_id] = game

  #return jsonify({'created':game})
  return jsonify(isError= False,
                    message= "New Game is Created",
                    statusCode= 200,
                    data=game), 200


#POST /api/games/<id>: Update the Game with the given ID, replacing its data with the newly POSTed data.
@app.route("/api/games/<int:game_id>", methods=['POST'])
def update_a_game(game_id):

  #POST data have "player, "symbol", "number", "size" information. Use them to update the game board dataframe and check if there is a winner
  
  #Search for the game_id in the DB, if game_id doesn't exist, abort it
  abort_if_not_exist(game_id)

  #process the POST data to get the updated game information
  modified_game = request.json

  #Player change the game board by selecting a number
  player = modified_game.get('player')
  size = modified_game.get('size') #game size
  symbol = modified_game.get('symbol')
  number = modified_game.get('number')
  
  logger.info("player = " + player)
  logger.info("symbol = " + symbol)
  logger.info("number = " + number)
  logger.info("number = " + number)

  #update the game board with this game_id in the DB
  
  #convert number to (row, col)
  mapping = Utility().mapNumberToTableCellIndex(size)
  (row, col) = mapping(number)

  #get the game board string from DB, map the string back to dataFrame. 
  #then update the dataFrame with the value in (row, col). Save the new data in DB

  #update the play_history with this game_id in the DB

  #check the game board wether there is a winner or not

  return json.dumps(default=lambda o: o.__dict__, sort_keys=True, indent=4)


if __name__ == "___main___":
  app.run(debug=True)

