from .__init__ import app
from .__init__ import sql_query

@app.route("/table/<x>")
def api_return_table(x):
    return sql_query("SELECT * FROM {}".format(x))

