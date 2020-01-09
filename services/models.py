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
