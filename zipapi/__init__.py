from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)



def sql_query(y):
    conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'), user=os.environ.get('DB_USER_NAME'), password=os.environ.get('DB_PWD'), host=os.environ.get('DB_HOST'))
    cur = conn.cursor()
    cur.execute("{}".format(y))
    row_headers=[x[0] for x in cur.description]
    tables = cur.fetchall()
    jsontable = []
    for result in tables:
        jsontable.append(dict(zip(row_headers, result)))
    return jsonify(jsontable)




@app.route('/')
def index():
    return '<p>index page</p>'


app.run()
from zipapi.api_table import *
