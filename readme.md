## How to run

When testing you must install the application each time using the following commands 

    $ export FLASK_APP=zipapi
    $ pip install -e .
    $ flask run









## Creating new Queries

New queries should follow the below template with your desired path in the place of URL_PATH

    from .__init__ import app
    from .__init__ import sqlQuery

    @app.route("/URL_PATH/<x>")
        def api_return_table(x):
        return sqlQuery("SELECT * FROM {}".format(x))

URL paths can be passed down by being placed within "<>" as described [here](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing)
