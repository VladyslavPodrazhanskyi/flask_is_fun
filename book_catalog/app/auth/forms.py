from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import EqualTo, DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField("Input your name: ", validators=[DataRequired(), Length(3, 25, message='between 3 and 25 characters')])
    email = StringField("Input your email: ", validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='passwords must be equal')])
    confirm = PasswordField('confirm', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField("Input your email: ", validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(5)])
    submit = SubmitField('Login')
