from pprint import pprint
from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config.update(
#     SECRET_KEY=b'\x84\xeb\xf3*o\x06\xfeX\xd6\x1b]$9\xa8)2\xdd\xaaLkxa\xc90',
#     # SQLALCHEMY_DATABASE_URI='<database>://<user.id>:<password>@<server>/<db_name>',
#     SQLALCHEMY_DATABASE_URI='postgresql://postgres:<???>@localhost/catalog_db,
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )
# Config of postgres DB cursor
# DATABASE = {
#     "database": "cursor_db",
#     "user": "cursor",
#     "password": "very_secret_password",
#     "port": 5432

#
# db = SQLAlchemy(app)


table = {'movie_1': 134.23,
         'movie_2': 85.152,
         'movie_3': 114.65,
         'movie_4': 184.09,
         'movie_5': 49.13,
         'movie_6': 78.8,
         'movie_7': 201.00,
         'movie_8': 125.7,
         'movie_9': 97.1,
         'movie_10': 78}


@app.route('/index')
@app.route('/')
def hello_flask():
    return "Hello, Flask!"


@app.route('/new/')
def query_strings(greeting="Hello"):
    query_val = request.args.get('greeting', greeting)
    pprint(request.args)
    return f"<h1>The greeting is {query_val}</h1>"


@app.route('/user/')
@app.route('/user/<name>')
def no_query_string(name='Mila'):
    return f'Hello, there!, {name}'


@app.route('/table')
def table_view():
    name = 'Vlad'
    return render_template('movies.html', name=name, table=table)

@app.route('/filters')
def filters():
    name = None
    film = "Christmas Evening"
    return render_template('filters.html', table=table,
                           name=name, film=film)

@app.route('/macros')
def jinja_macros():
    return render_template('using_macros.html', movies=table)

if __name__ == "__main__":
    app.run(debug=True)