import flask
from flask import json
from flask import request
from flask_restful import Resource, Api, reqparse


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/', methods = ['POST'])
def api_message():
        return request.data  
app.run()
