from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zwnlkqhnfyaxnh:GFkT10cJtu6REr91W_Xlj7ePMF@ec2-107-22-170-249.compute-1.amazonaws.com:5432/dfe8besv4oq9ol'
db = SQLAlchemy(app)


class Market(db.Model):
    __tablename__ = 'globuses'
    id = db.Column(db.Integer, primary_key=True)
    lbactive = db.Column(db.Float())
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
