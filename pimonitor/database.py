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
