from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import EqualTo, DataRequired, Length, Email, ValidationError
from app.auth.models import User

def email_exists(form, field):
    user = User.query.filter_by(email=field.data).first()
    if user:
        raise ValidationError('User with this email exists!')



class RegistrationForm(FlaskForm):
    name = StringField("Input your name: ", validators=[DataRequired(), Length(3, 25, message='between 3 and 25 characters')])
    email = StringField("Input your email: ", validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='passwords must be equal')])
    confirm = PasswordField('confirm', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField("Input your email: ", validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(5)])
    # Handle the normally-tricky “remember me” functionality.
    stay_loggedin = BooleanField('stay logged-in')  #check box
    submit = SubmitField('Login')

# https://flask-login.readthedocs.io/en/latest/