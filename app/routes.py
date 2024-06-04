from app import app
from flask import render_template

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
   