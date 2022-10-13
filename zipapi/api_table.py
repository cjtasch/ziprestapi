from .__init__ import app
from .__init__ import sqlQuery

@app.route("/table/<x>")
def api_return_table(x):
    return sqlQuery("SELECT * FROM {}".format(x))

