from app import app, db
from flask import render_template, redirect, flash, url_for, request
from app.forms import  LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user,  login_user, logout_user, login_required
from app.models import User
from urllib.parse import urlsplit
from datetime import datetime, timezone


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
            return redirect(url_for("index"))

        return redirect(url_for("index"))
    

    return render_template("login.html", form=form, title="Log In")
    


@app.route("/register", methods=["POST", "GET"])
def register():

    ## incase some onwe who is already logged in try to register
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
            
        username = form.username.data
        email = form.email.data.lower()
        password = form.password.data

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash(f"congratulations, {username}! you a now registered")
        return redirect(url_for("login"))


    return render_template("register.html", form=form, title ="Sign Up")


@app.route("/user/<username>")
@login_required
def user(username):

    user = User.query.filter_by(username=username).first_or_404()
    posts= [{"author":"user", "body":"test post 1"}, 
             {"author":"user", "body":"test post "}]
    

    ## dear future me, incase you wonder why i didnt use current_user in user.html, i passed user instead
    ##to user.html, beacuse a user may want to access another's profile

    return render_template("user.html", user=user, posts= posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()


@app.route("/edit_profile", methods=["POST", "GET"])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data

        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        #in case of a refresh, to ensure that the form fields are pre-filled with the current 
       # user's data when the page is loaded 
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template("edit_profile.html", form = form, title="Edit Profile")
    


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

