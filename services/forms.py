# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import required, optional, Length, Email, Regexp, DataRequired, EqualTo

from .models import SurveyInfo


class SurveyForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Length(1, 64), Email()])
    interests = StringField('Research area of ​​interest', validators=[
        DataRequired(), Length(1, 64)])
    year = StringField('Which year are you in the university', validators=[
        DataRequired(), Length(1, 64)])
