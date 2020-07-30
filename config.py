from os import environ

import psycopg2
from dotenv import load_dotenv
from flask import Flask


# load the .env file and create flask app instance
load_dotenv('./.env')
app = Flask(__name__)

# set up the database
user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')
host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
database = environ.get('DB_NAME')


def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=database, user=user, password=password, host=host, port=port)
        return conn
    except psycopg2.Error as e:
        return str(e)


conn = connect_db()
