from . import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm


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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)