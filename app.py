from flask import Flask, send_from_directory
import uuid

app = Flask(__name__, static_url_path='')

@app.route('/api/render', methods=['POST', 'GET'])
def render():
    filename = str(uuid.uuid4())
    return filename, 200

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
