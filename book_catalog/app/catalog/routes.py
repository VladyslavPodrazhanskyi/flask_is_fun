# app/catalog/routes.py
from flask import render_template
from app.catalog import main
from app.catalog.models import Book, Publication

@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/display/publisher/<int:publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.get(publisher_id)
    publisher_books = Book.query.filter_by(pub_id=publisher_id).all()
    return render_template('publisher.html', publisher_books=publisher_books, publisher=publisher)
