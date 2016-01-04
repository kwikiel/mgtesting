from flask import Flask, render_template, jsonify
from models import Market
from models import db
app = Flask(__name__)


@app.route("/init")
def start():
    db.create_all()
    db.session.commit()
    return "yolo"


@app.route("/")
def hello():
    ping = Market.query.first()
    return render_template("index.html", data=ping)


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/papiez.json")
def ret():
    return jsonify({'data': [
        {
            'date': c.created.strftime('%Y-%m-%d'),
            'value': c.lbactive,
        } for c in Market.query.all()
    ]})
