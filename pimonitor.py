from flask import Flask, request
import json
import psycopg2
import configparser

app = Flask(__name__)

def db_connect():
    Config = configparser.ConfigParser()
    Config.read("config.ini")

    if Config.sections():
        try:
            conn = psycopg2.connect(
                host=Config.get('postgres','host'),
                database=Config.get('postgres', 'database'),
                user=Config.get('postgres', 'user'),
                password=Config.get('postgres', 'password'),
                port=Config.get('postgres', 'port')
            )

            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            raise(error)
    else:
        return None

def load(data):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        
        SQL = "INSERT INTO home_data (location, timestamp, temperature, humidity) VALUES (%s, %s, %s, %s);"
        
        for sensor in data['sensors']:
            cursor.execute(SQL, (data['location'], data['timestamp'], sensor['temperature'], sensor['humidity']))
            
            conn.commit()
            cursor.close()
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

@app.route('/', methods=['POST'])
def result():
    if request.is_json:
        content = request.get_json()
        load(content)
        ack = '[' + content['timestamp'] + '] Successfully received and inserted into database.'
    else:
        ack = 'An unexpected error occured.  Try again.'
    return ack

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
