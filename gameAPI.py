#Rest API for Tic Tac Toe

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, marshal_with, fields, abort
import json
import random

app = Flask(__name__)
api = Api(app)

#games information should come from DB. To be implemented
games={{'game_id': "1", 'player1':  "Chi", 'player2': "Joanna", },
        {'game_id': "2", 'player1': "Bing", 'player2': "Jing"},
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
  Two way to assign an id toa new game
  #1. Randomly generate a game_id, and make sure the id has not been used
  #2. Always increament the length of games by 1. Use #2 here
  """
  game_id = len(games)+1

  #Do POST in postman to send the request to the server
  #use the players information from the POST to create a new game
  name1 = 
  #create a new game

  game = {'game_id': game_id, 'player1': "Jack", 'player2': "Mike"}

  #add the new game
  games[game_id] = game

  
  #create a new game


  return jsonify({'created':game})



#POST /api/games/<id>: Update the Game with the given ID, replacing its data with the newly POSTed data.
@app.route("/api/games/<int:game_id>", methods=['POST'])
def update_game(game_id):

  abort_if_not_exist(game_id)
  
  modifiedGame = request.json

  found = games[game_id]
  found.row = modifiedGame["row"]

  if(not found):
    abort(404, description="game_id does not exist")

   #update found logic 
 

  return json.dumps(found, default=lambda o: o.__dict__, sort_keys=True, indent=4)





if __name__ == "___main___":
  app.run(debug=True)




#games.append(game)

  #return jsonify({'created':game})
  return jsonify(isError= False,
                    message= "New Game is Created",
                    statusCode= 200,
                    data=newgame), 200



def json2Game(mutildictObj):
    game_id = mutildictObj["game_id"]
    game = Game(game_id, mutildictObj["player1"], mutildictObj["player2"], mutildictObj["row"])
    return game_id, game


@app.route("/api/games/<int:game_id>", methods=['POST'])
def update_game(game_id):
  #found = any(d['game_id'] == str(game_id) for d in games)
  modifiedGame = request.json
  found = games[game_id]
  found.row = modifiedGame["row"]

  if(not found):
    abort(404, description="game_id does not exist")

   #update found logic 
 

  return json.dumps(found, default=lambda o: o.__dict__, sort_keys=True, indent=4)


if __name__ == "___main___":
  app.run(debug=True)

"""
class Game:
    def __init__(self, id, player1, player2, row):
        self.game_id = id
        self.player1 = player1
        self.player2 = player2
        #test field
        self.row = row


        print("=== init game: ", id, player1, player2)
"""


