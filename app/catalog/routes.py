# app/catalog/routes.py
from flask import (render_template, request, redirect,
                   url_for, flash)
from app.catalog import main
from app.catalog.models import Book, Publication
from app.catalog.forms import DeleteForm, EditForm, AddForm
from flask_login import login_required
from app import db


@main.route('/')
def display_books():
    books = Book.query.all()
    for k, v in request.args.items():
        print(k, v)
    return render_template('home.html', books=books)


@main.route('/display/publisher/<int:publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.get(publisher_id)
    publisher_books = Book.query.filter_by(pub_id=publisher_id).all()
    return render_template('publisher.html', publisher_books=publisher_books, publisher=publisher)


@main.route('/book/delete/<int:book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        flash('The book was successfully deleted!')
        return redirect(url_for('main.display_books'))
    return render_template('delete.html', book=book)


# @main.route('/delete/<int:book_id>', methods=['GET', 'POST'])
# @login_required
# def delete_book(book_id):
#     book = Book.query.get(book_id)
#     form = DeleteForm()
#     if form.validate_on_submit():
#         db.session.delete(book)
#         db.session.commit()
#         flash('The book was successfully deleted!')
#         return redirect(url_for('main.display_books'))
#     return render_template('delete.html', book=book, form=form)


@main.route('/book/edit/<int:book_id>', methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditForm(obj=book) # # добавление объекта обеспечивает автозаполение при GET запросе
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('The book edited successfully!')
        return redirect(url_for('main.display_books'))
    return render_template('edit.html', form=form, book=book)


@main.route('/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = AddForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            avg_rating=form.avg_rating.data,
            format=form.format.data,
            image=form.image.data,
            num_pages=form.num_pages.data,
            pub_id=form.pub_id.data
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('main.display_books'))
    return render_template('add.html', form=form)


@main.app_errorhandler(404)
def not_found(e):
    return render_template('not_found.html'), 404
