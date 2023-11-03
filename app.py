# save this as app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(username='eduCBA' ,
    account='Premium' ,
    validity='200 days')