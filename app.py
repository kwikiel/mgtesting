from flask import Flask
from flask import render_template
from models import Market
from models import db
import json
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
    return render_template("base.html")


@app.route("/data.json")
def ret():
    raw = Market.query.all()
    cooked = json.dumps([d.lbactive for d in raw])
    return render_template("fake_users1.json", cooked=cooked)

app.run(debug=True)
