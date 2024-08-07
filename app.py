from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the directory where your GZIP files and index.html are stored
BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(BASE_DIRECTORY, 'index.html')

@app.route('/<path:filename>')
def serve_gzip(filename):
    # Serve GZIP files with correct headers
    if filename.endswith('.gz'):
        file_path = os.path.join(BASE_DIRECTORY, filename)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
            return data, 200, {'Content-Encoding': 'gzip', 'Content-Type': 'application/javascript'}
    
    return send_from_directory(BASE_DIRECTORY, filename)

if __name__ == '__main__':
    app.run(debug=True)
