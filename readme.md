## How to run

When testing you must install the application each time using the following commands 

    $ pip install -e .
  









## Creating new Queries

New queries should follow the below template with your desired path in the place of URL_PATH

    from .__init__ import app
    from .__init__ import sqlQuery

    @app.route("/URL_PATH/<x>")
        def api_return_table(x):
        return sqlQuery(f"SELECT * FROM {x}")

URL paths can be passed down by being placed within "<>" as described [here](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing)

URL arguements can be accessed as described [here](https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask)

the sqlQuery method can then be used to send a query directly to the DB. 