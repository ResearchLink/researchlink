# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, SelectField
from wtforms.validators import required, optional, Length, Email, Regexp, DataRequired, EqualTo

from .models import SurveyInfo


class SurveyForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()])
    interests = StringField('Research area of interest', validators=[
        DataRequired(), Length(1, 64)])
    year = StringField('Which year are you in the university', validators=[
        DataRequired(), Length(1, 64)])


class ProfileForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()])
    name = StringField('What\'s your name', validators=[
        DataRequired(), Length(1, 64)])
    major = StringField('What\'s your major', validators=[
        DataRequired(), Length(1, 64)])
    education = StringField('What\'s your university', validators=[
        DataRequired(), Length(1, 64)])
    year = SelectField('Education', choices=[
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
        ('Postdoc', 'Postdoc')
    ])
    interests = StringField('Research area of interest', validators=[
        DataRequired(), Length(1, 64)])
