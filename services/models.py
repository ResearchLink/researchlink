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
    abstract = db.Column(db.String(256))
    body = db.Column(db.Text)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img_addr = db.Column(db.String(140))

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(80))
    name = db.Column(db.String(80))
    major = db.Column(db.String(80))
    education = db.Column(db.String(80))
    year = db.Column(db.String(80))
    interests = db.Column(db.String(80))

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
