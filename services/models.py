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
    __tablename__  = "Post"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img_addr = db.Column(db.String(140))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
