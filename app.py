import chess.pgn, chess.svg
from flask import Flask, send_from_directory, request
import io
import json
import uuid

app = Flask(__name__, static_url_path='')

@app.route('/api/render', methods=['POST', 'GET'])
def render():
    # Generate a unique id for the result
    filename = str(uuid.uuid4())
    data = request.json

    # Render the page
    game = chess.pgn.read_game(io.StringIO(data['gameData']))
    board = game.board()
    for move in game.mainline_moves():
        board.push(move)
    outFile = open("./static/rendered/{}.svg".format(filename), "w")
    outFile.write(chess.svg.board(board, size=350))
    outFile.close()

    print(request.json)
    return json.dumps({ 'id': filename }), 200

# Serve static content - Replace with proper static site
# in production
@app.route('/', methods=['GET'])
def serve_index():
    return serve_static_files("index.html")

@app.route('/<path:path>', methods=['GET'])
def serve_static_files(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True)
