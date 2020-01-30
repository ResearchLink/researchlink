# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    SubmitField, ValidationError, SelectField, TextAreaField, DateTimeField
from wtforms.validators import required, optional, Length, Email, Regexp, DataRequired, EqualTo


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


class IdeaForm(FlaskForm):
    idea = TextAreaField('Idea', validators=[DataRequired()])


class PostForm(FlaskForm):
    position = StringField('Position', validators=[
        DataRequired()])
    lab = StringField('Lab', validators=[
        DataRequired()])
    details = TextAreaField('Details', validators=[
        DataRequired()])
    requirements = TextAreaField('Requirements', validators=[
        DataRequired()])
    img_addr = StringField('Upload the link of the lab logo', validators=[
        DataRequired()])
    key_words = StringField('key_words', validators=[
        DataRequired()])


class SeminarForm(FlaskForm):
    seminar_name = StringField('seminar_name', validators=[
        DataRequired()])
    title = StringField('title', validators=[
        DataRequired()])
    speaker_name = StringField('speaker_name', validators=[
        DataRequired()])
    speaker_department = StringField('speaker_department', validators=[
        DataRequired()])
    speaker_description = StringField('speaker_description', validators=[
        DataRequired()])
    time = StringField('time', validators=[
        DataRequired()])
    address = StringField('address', validators=[
        DataRequired()])
    abstract = TextAreaField('abstract', validators=[
        DataRequired()])
    key_words = StringField('key_words', validators=[
        DataRequired()])
