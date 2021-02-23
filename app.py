from flask import Flask, render_template, url_for
from forms import SignUpForm
from wtforms.validators import DataRequired


app= Flask(__name__)
app.config['SECRET_KEY'] = 'lozinka'
@app.route("/")
def home():
    return render_template("html1.html")
@app.route("/pecanje")
def pecanje():
    return render_template("html2.html")
@app.route("novosti")
def novosti():
    forms=SignUpForm()
    return render_template("html3.html", form=forms)
app.run()
