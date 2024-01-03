# importing the class "Flask" which create website object instances
from flask import Flask, render_template

app = Flask("Website")

# applying route method to the object app
# make sure to add the html pages inside the "templates" folder 
# the images has to be in a folder called "static"
# and render them through the render_template function

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact-us/")
def contact():
    return render_template("contact-us.html")

@app.route("/store/")
def store():
    return render_template("store.html")

app.run(debug = True)
