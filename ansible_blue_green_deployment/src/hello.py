from flask import Flask
import os

app = Flask(__name__)
version = os.environ['APP_VERSION']

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/version')
def show_version():
    return version

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
