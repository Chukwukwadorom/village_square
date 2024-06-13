from app import app, db
from flask import render_template, redirect, flash, url_for, request
from app.forms import  LoginForm, RegistrationForm
from flask_login import current_user,  login_user, logout_user, login_required
from app.models import User
from urllib.parse import urlsplit


@app.route('/')
@app.route('/index')
@login_required
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
    

    return render_template("index.html", posts=posts, title="Home") 


@app.route('/login', methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    print("here")
    
    form = LoginForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash("incorrect username or password")
            return redirect(url_for("login"))
        
        login_user(user, remember = form.remember_me.data)
        flash(f"logging in {form.username.data}, remember me: {form.remember_me.data}")

        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(url_for(index))

        return redirect(url_for("index"))
    

    return render_template("login.html", form=form, title="Log In")
    


@app.route("/register", methods=["POST", "GET"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
            
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username=username, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("congratulations! you a now registered")
        return redirect(url_for("login"))


    return render_template("register.html", form=form, title ="Sign Up")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))