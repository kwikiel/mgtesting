from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import urlparse

urlparse.uses_netloc.append("postgres")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    urlparse.urlparse(os.environ["DATABASE_URL"])
db = SQLAlchemy(app)


class Market(db.Model):
    __tablename__ = 'globuses'
    id = db.Column(db.Integer, primary_key=True)
    lbactive = db.Column(db.Float())
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id, lbactive, created):
        self.id = id
        self.lbactive = lbactive
        self.created = created

    def __repr__(self, id, lbactive, created):
        return "<Date: {0} Active: {1}>".format(self.created, self.lbactive)
