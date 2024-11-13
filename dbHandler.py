import sqlite3

def create_connection():
    connection = sqlite3.connect('current.db', uri=True)
    print("Connection established!")
    connection.cursor()
    return connection

def close_connection(connection):
    connection.commit()
    connection.close()