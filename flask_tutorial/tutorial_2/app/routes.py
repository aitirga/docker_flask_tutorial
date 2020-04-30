from . import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Aitor"}
    posts = [
        {
            "author": {"username": "Aitor"},
            "body": "Beautiful day in Barcelona",
        },
        {
            "author": {"username": "Gerard"},
            "body": "I am doing a puzzle",
        },
        {
            "author": {"username": "Nuria"},
            "body": "Villagato is fun!",
        },
        {
            "author": {"username": "Uri"},
            "body": "I love watching JetLag",
        },
    ]
    return render_template("index.html",
                           title="home",
                           user=user,
                           posts=posts,
                           )

