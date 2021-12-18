import os
import json
from flask import Flask, jsonify, abort, make_response, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

## Routes

@app.route("/")
@app.route("/home")
def home():
    return render_template("zmoodwebui.html", title="Zmood WebUI v0.1");

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 - Not found'}), 404)

@app.errorhandler(503)
def not_found(error):
    return make_response(jsonify({'error': '503 - There was an error.'}), 503)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080)
