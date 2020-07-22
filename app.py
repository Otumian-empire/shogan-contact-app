from os import environ

import psycopg2
from dotenv import load_dotenv
from flask import Flask


load_dotenv('./.env')
app = Flask(__name__)

user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')
host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
database = environ.get('DB_NAME')


@app.route('/', methods=['GET', 'POST'])
def home():

    try:
        conn = psycopg2.connect(
            dbname=database, user=user, password=password, host=host, port=port)
        if conn:
            return '123'
        else:
            return '321'
    except psycopg2.Error as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
