from flask import Flask, render_template, jsonify
from models import Market
app = Flask(__name__)


@app.route("/")
def hello():
    return "/test for chart and /trigger for trg"


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/papiez.json")
def ret():
    return jsonify({'data': [
        {
            'date': c.created.strftime('%Y-%m-%d %H:%M:%S'),
            'value': c.lbactive,
        } for c in Market.query.all()
    ]})
