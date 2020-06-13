# app/catalog/routes.py
from flask import render_template
from app.catalog import main
from app.catalog.models import Book, Publication

@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('books.html', books=books)


