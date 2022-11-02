from urllib import request
from .__init__ import app
from .__init__ import sql_query


@app.route("/state/<x>")
def api_return_zipbystate(x):
    return sql_query(f'SELECT ZIP_CODE FROM zip WHERE STATE = "{x.upper()}"')

@app.route("/cityzip/<x>/<y>")
def api_return_zipbycity(x, y):
    return sql_query(f'SELECT ZIP_CODE FROM zip WHERE PO_NAME LIKE "{y}" AND STATE = "{x.upper()}"')