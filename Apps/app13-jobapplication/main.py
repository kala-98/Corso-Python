from datetime import datetime
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" # specifying we want to use sqlite
db = SQLAlchemy(app)

class Form(db.Model):
    # creating the structure
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"] # it's the "name" from the input tag in html
        last_name = request.form["last_name"]        
        email = request.form["email"] 
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["employment_status"] 

        form = Form(first_name = first_name, last_name = last_name,
                    email = email, date = date_obj, occupation = occupation)
        db.session.add(form)
        db.session.commit()
        flash(f"{first_name}, your form submitted successfully!", "success")
        
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug = True, port = 5001)
