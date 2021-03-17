from pimonitor import app
from pimonitor.database import *

from flask import request
import json

@app.route('/', methods=['POST'])
def result():
    if request.is_json:
        content = request.get_json()
        load(content)
        ack = '[' + content['timestamp'] + '] Successfully received and inserted into database.'
    else:
        ack = 'An unexpected error occured.  Try again.'
    return ack

@app.route('/index')
def index():
    return 'Hello, World!'    
