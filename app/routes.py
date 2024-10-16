import os

from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from app import app


@app.route("/")
@app.route("/home")
def home():
    user = {"username": "Armin"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful in Portland"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool"},
    ]

    return render_template("home.html", title="Home", user=user, posts=posts)
