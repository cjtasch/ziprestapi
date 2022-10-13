from flask import Flask, jsonify
import psycopg2


app = Flask(__name__)



def sqlQuery(y):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
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
