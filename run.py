from pprint import pprint
from flask import Flask, request, render_template, url_for


app = Flask(__name__)


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


@app.route('/user')
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


if __name__ == "__main__":
    app.run(debug=True)