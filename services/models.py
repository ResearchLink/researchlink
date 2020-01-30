from flaskweb.app import db
from datetime import datetime
import json


class SurveyInfo(db.Model):
    __tablename__ = 'SurveyInfo'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    interests = db.Column(db.String(80))
    year = db.Column(db.String(80))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<SurveyInfo %r>' % self.email


class Post(db.Model):
    __tablename__ = "Post"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    lab = db.Column(db.Text)
    position = db.Column(db.Text)
    details = db.Column(db.Text)
    requirements = db.Column(db.Text)
    key_words = db.Column(db.Text)
    img_addr = db.Column(db.Text)

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # lab_name = db.Column(db.String(140))
    # abstract = db.Column(db.String(256))
    # body = db.Column(db.Text)
    # requirements = db.Column(db.Text)
    # about = db.Column(db.Text)
    # # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # img_addr = db.Column(db.String(140))
    # tags = db.Column(db.String(256))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Application(db.Model):
    __tablename__ = "Application"

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer)
    resume_addr = db.Column(db.String(140))

    def __repr__(self):
        return '<Application {}>'.format(self.resume_addr)


class Profile(db.Model):
    __tablename__ = "Profile"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(80))
    name = db.Column(db.String(80))
    major = db.Column(db.String(80))
    education = db.Column(db.String(80))
    year = db.Column(db.String(80))
    interests = db.Column(db.String(80))

    # this is for profs
    title = db.Column(db.String(80))
    bio = db.Column(db.Text)

    def __repr__(self):
        return '<Profile {}>'.format(self.email)


class Idea_Post(db.Model):
    __tablename__ = "Idea_Post"

    id = db.Column(db.Integer, primary_key=True)
    abstract = db.Column(db.String(140))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Idea_Post {}>'.format(self.body)


class Idea_Comments(db.Model):
    __tablename__ = "Idea_Comments"

    id = db.Column(db.Integer, primary_key=True)
    idea_post_id = db.Column(db.Integer)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # img_addr = db.Column(db.String(140))

    def __repr__(self):
        return '<Idea_Comments {}>'.format(self.body)


class Seminars(db.Model):
    __tablename__ = "Seminars"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    seminar_name = db.Column(db.Text)
    title = db.Column(db.Text)
    speaker_name = db.Column(db.Text)
    speaker_department = db.Column(db.Text)
    speaker_description = db.Column(db.Text)
    time = db.Column(db.Text)  # the time the seminar happens
    address = db.Column(db.Text)
    abstract = db.Column(db.Text)
    key_words = db.Column(db.Text)

    def __repr__(self):
        return '<Seminar {}>'.format(self.title)
