from datetime import datetime

from pprint import pprint
from flask import Flask, request, render_template, url_for, session, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SECRET_KEY=b'\x84\xeb\xf3*o\x06\xfeX\xd6\x1b]$9\xa8)2\xdd\xaaLkxa\xc90',
    # SQLALCHEMY_DATABASE_URI='<database>://<user.id>:<password>@<server>/<db_name>',
    SQLALCHEMY_DATABASE_URI='postgresql://pvv:krpp@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


db = SQLAlchemy(app)


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


@app.before_request
def some_function():
    g.string = '<br> This runs before any request'


@app.route('/index')
@app.route('/')
def hello_flask():
    return "Hello, Flask!" + g.string


@app.route('/new/')
def query_strings(greeting="Hello"):
    query_val = request.args.get('greeting', greeting)
    pprint(request.args)
    return f"<h1>The greeting is {query_val}</h1>" + g.string
    # http://127.0.0.1:5000/new/?greeting=Hi!


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


@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'Garry'
        return render_template('session.html', session=session, name=session['name'])


class Publication(db.Model):
    __tablename__ = 'publications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name
    #   self.id = id

    def __repr__(self):
        return f'Publisher is {self.name}'


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String, unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publications.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return f'{self.title} by {self.author}'



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)