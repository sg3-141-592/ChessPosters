import chess.pgn, chess.svg
from flask import Flask, send_from_directory, request
import io
import json
import os
import renderBoard
import uuid

app = Flask(__name__, static_url_path='')

@app.route('/api/render', methods=['POST', 'GET'])
def render():
    data = request.json
    return json.dumps({
        'id': renderBoard.generatePreview(io.StringIO(data['gameData']))
    }), 200

# Serve static content - Replace with proper static site
# in production
@app.route('/', methods=['GET'])
def serve_index():
    return serve_static_files("index.html")

@app.route('/<path:path>', methods=['GET'])
def serve_static_files(path):
    return send_from_directory('static', path)

# Clear tmp directory on start-up
for filename in os.listdir('tmp'):
    os.remove('tmp/'+filename)

if __name__ == "__main__": 
    app.run(debug=True)
