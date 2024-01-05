# importing the class "Flask" which create website object instances
from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, static_url_path='/static')

df = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/api/v1/<word>")
def api(word):
    word = word.lower()
    definition = df.loc[df["word"] == word]["definition"]

    if definition.dropna().empty:
        definition = f"The word {word} does not exist"
    else:
        definition = definition.squeeze()
    return {"definition": definition,
            "word": word}

if __name__ == "__main__":
   app.run(debug = True, port = 5000)