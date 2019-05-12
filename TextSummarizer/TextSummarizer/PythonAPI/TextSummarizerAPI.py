import flask
import requests
from flask import json
from flask import request
from flask_restful import Resource, Api, reqparse
from gensim.summarization.summarizer import summarize

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<p>This is a test GET End point</p>"


@app.route('/', methods = ['POST'])
def api_message():
    text=request.data.strip().decode('utf-8')
    return summarize(text)
app.run()
