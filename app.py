from flask import Flask
from flask import render_template
from models import Market
from models import db
app = Flask(__name__)


@app.route("/init")
def start():
    db.create_all()
    test = Market(id=1337, lbactive=3.14,None)
    db.session.add(test)
    db.session.commit()

@app.route("/")
def hello():
    ping = Market.query.all()
    return render_template("index.html", data=ping)
