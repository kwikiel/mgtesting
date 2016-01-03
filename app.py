from flask import Flask
from flask import render_template
from models import Market
from models import db
app = Flask(__name__)


@app.route("/init")
def start():
    db.create_all()
    test = Market(id=1335, lbactive=3.14)
    db.session.add(test)
    db.session.commit()
    return "yolo"


@app.route("/")
def hello():
    ping = Market.query.all()
    return render_template("index.html", data=ping)


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/data/fake_users1.json")
def ret():
    return render_template("fake_users1.json")
