from pimonitor import app
from pimonitor.database import *

from flask import request, abort
import json

@app.route('/', methods=['POST'])
def default_post():
    # Automatically deny non-JSON posts
    # Automatically deny invalid API keys
    try:
        assert request.is_json
        
        # Load JSON data from post
        # get_json automatically returns 400 error if invalid JSON
        content = request.get_json()
        
        if validate_hash(content['api_hash']) == False:
            abort(403, 'Invalid API Key')
            
    except AssertionError:
        abort(400, 'Content type must be \'application/json\'')
    except psycopg2.OperationalError:
        abort(500, 'Unable to connect to database')
    except psycopg2.errors.UndefinedTable:
        abort(500, 'Unexpected database configuration')
    except psycopg2.DatabaseError:
        abort(500, 'Database action failed')

    # Insert JSON data into database
    try:
        load(content)
    except AssertionError:
        abort(400, 'Incomplete request')
    except psycopg2.OperationalError as error:
        abort(500, 'Unable to connect to database')
    except psycopg2.errors.UndefinedTable as error:
        abort(500, "Unexpected database configuration")
    except psycopg2.DatabaseError as error:
        abort(500, "Database action failed")

    # Acknowledge success
    return "Success\n"

@app.route('/index')
def index():
    return 'Hello, World!'
