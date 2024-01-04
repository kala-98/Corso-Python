# importing the class "Flask" which create website object instances
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/api/v1/<word>")
def api(word):
    return {"definition": word.upper(),
            "word": word}

if __name__ == "__main__":
   app.run(debug = True, port = 5000)