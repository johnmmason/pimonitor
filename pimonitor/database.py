import psycopg2
import configparser

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
    if validate_hash(data['api_hash']):
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
            return True
    else:
        return None

def validate_hash(key_hash):
    try:
        conn = db_connect()
        cursor = conn.cursor()

        SQL = "SELECT * FROM api_keys WHERE hash = (%s);"

        cursor.execute(SQL, (key_hash,))
        results = cursor.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

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
