from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect

import json

from BarBeerDrinker import database

app = Flask(__name__)
@app.route('/api/ratings', methods=["GET"])
def get_ratings():
    return jsonify(database.get_ratings())

