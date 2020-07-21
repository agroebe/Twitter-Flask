from flask import Flask
from flask_cors import CORS

import os

from api import api_blueprint

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=os.environ['DEBUG'] == 'True', host='0.0.0.0')