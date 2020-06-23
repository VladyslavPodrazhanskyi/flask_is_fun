#app/catalog/forms.py

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class DeleteForm(FlaskForm):
    delete = SubmitField('delete')


class EditForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    author = StringField('Author:', validators=[DataRequired()])
    format = StringField('Format:', validators=[DataRequired()])
    num_pages = IntegerField('Pages:', validators=[DataRequired()])
    submit = SubmitField('edit')


class AddForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    author = StringField('Author: ', validators=[DataRequired()])
    avg_rating = FloatField('Rating: ', validators=[DataRequired()])
    format = StringField('Format: ', validators=[DataRequired()])
    image = StringField('Images: ', validators=[DataRequired()])
    num_pages = IntegerField('Pages: ', validators=[DataRequired()])
    pub_id = IntegerField('Pub_id: ', validators=[DataRequired()])
    submit = SubmitField('Add')

