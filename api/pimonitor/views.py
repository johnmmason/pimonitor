from pimonitor import app
from pimonitor.database import *

from flask import request
import json

@app.route('/', methods=['POST'])
def result():
    if request.is_json:
        content = request.get_json()
        if load(content) is not None:
            ack = '[' + content['timestamp'] + '] Successfully received and inserted into database.'
        else:
            ack = 'Invalid API Key'
    else:
        ack = 'Content was not json'
    return ack

@app.route('/index')
def index():
    return 'Hello, World!'
