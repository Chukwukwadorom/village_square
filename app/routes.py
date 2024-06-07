from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import  LoginForm

@app.route('/')
@app.route('/index')
def index():

    posts = [
        {
            'author': {'username': 'Kwado'},
            'body': "dont stop till we get enough"
        },
        {
            'author': {'username': 'Kwadont'},
            'body': 'Embrace Chaos!'
        }
    ]
    
    user = {"username":"Chikwado"}

    return render_template("index.html", posts=posts, title="Home", user=user) 


@app.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"logging in {form.username.data}, remember me: {form.remember_me.data}")
        return redirect(url_for("index"))

    return render_template("login.html", form=form, title="Log In")
    