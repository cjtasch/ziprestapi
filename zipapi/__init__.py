from http import server
import os
from flask import Flask, jsonify
import pyodbc
import sqlite3

app = Flask(__name__)

def connect_db():
    #con = sqlite3.connect('crosswalk.db')
    con = pyodbc.connect(database=os.environ.get('DB_NAME'), uid=os.environ.get('DB_USER_NAME'), pwd=os.environ.get('DB_PWD'), server=os.environ.get('DB_HOST'), driver='ODBC Driver 18 for SQL Server', TrustServerCertificate='yes')
    return con

def sql_query(y):
    con = connect_db()
    cur = con.cursor()
    print(f"{y}")
    cur.execute(f"{y}")
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
from zipapi.api_state import *