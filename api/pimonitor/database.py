import psycopg2
import configparser

def db_connect():
    Config = configparser.ConfigParser()
    Config.read("config.ini")

    if Config.sections():
        conn = psycopg2.connect(
            host=Config.get('postgres','host'),
            database=Config.get('postgres', 'database'),
            user=Config.get('postgres', 'user'),
            password=Config.get('postgres', 'password'),
            port=Config.get('postgres', 'port')
        )
        return conn
    else:
        return None

def load(data):
    assert 'location' in data.keys()
    assert 'timestamp' in data.keys()
    assert len(data['sensors']) > 0

    conn = db_connect()
    cursor = conn.cursor()
        
    SQL = "INSERT INTO home_data (location, timestamp, temperature, humidity) \
        VALUES (%s, %s, %s, %s);"
            
    for sensor in data['sensors']:
        cursor.execute(SQL, (data['location'],
                             data['timestamp'],
                             sensor['temperature'],
                             sensor['humidity']))                
        conn.commit()

    cursor.close()
    conn.close()        

def validate_hash(key_hash):
    conn = db_connect()
    cursor = conn.cursor()

    SQL = "SELECT * FROM api_keys WHERE hash = (%s);"

    cursor.execute(SQL, (key_hash,))
    results = cursor.fetchall()
        
    if results:
        return True
    else:
        return False

def add_hash(key_hash):
    try:
        conn = db_connect()
        cursor = conn.cursor()

        SQL = "INSERT INTO api_keys (hash, app) VALUES (%s, %s);"

        cursor.execute(SQL, (key_hash, "pimonitor"))

        conn.commit()
        cursor.close()

    finally:
        if conn is not None:
            conn.close()
