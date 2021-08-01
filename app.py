from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

# Serve static content - Replace with proper static site
# in production

@app.route('/')
def serve_index():
    return serve_static_files("index.html")

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()
