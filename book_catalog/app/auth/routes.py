# app/auth/routes

from flask import render_template, request, redirect, url_for, flash
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.auth.models import User
from flask_login import login_user, logout_user, login_required

@at.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit(): #check if method is POST and validate data in the form
        User.create_user(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('Registration is successful!')
        return redirect(url_for('authentication.login_user_view'))
    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def login_user_view():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_pass(form.password.data):
            login_user(user)
            flash('You are logged in')
            next = request.args.get('next')
            if next is None or next[0] != '/':
                next = url_for('main.display_books')
            return redirect(next)
    return render_template('login.html', form=form)


@at.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('main.display_books'))

