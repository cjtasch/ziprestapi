from http import server
import os
from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)



def sql_query(y):
    conn = pyodbc.connect(database=os.environ.get('DB_NAME'), uid=os.environ.get('DB_USER_NAME'), pwd=os.environ.get('DB_PWD'), server=os.environ.get('DB_HOST'), driver='{SQL Server Native Client 10.0}')
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


from zipapi.api_table import *
