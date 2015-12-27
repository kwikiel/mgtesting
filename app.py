from flask import Flask
from flask import render_template
from models import Market
app = Flask(__name__)


@app.route("/")
def hello():
    ping = Market.query.all()
    return render_template("index.html", data=ping)

if __name__ == "__main__":
    app.run(debug=True)
