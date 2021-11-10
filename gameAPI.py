#Rest API for Tic Tac Toe

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return "Welcome to Tic Tac Toa API"

games=[ {'game_id': "1", 'player1': "Chi", 'player2': "CJ"},
        {'game_id': "2", 'player1': "Bing", 'player2': "Jing"},
        {'game_id': "3", 'player1': "Andrew", 'player2': "Mark"}
      ]

app = Flask(__name__)

@app.route("/api/games", methods=['GET'])
def get():
  return jsonify({'games':games})


if __name__ == "___main___":
  app.run(debug=True)

