from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Render the login page with the login form.

    Returns:
        Response: The HTML content for the login page with the title 'Sign In'.
    """
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect(url_for("home"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/")
@app.route("/home")
def home():
    """
    Renders the home page with user information and a list of posts.

    Returns:
        str: The rendered HTML content for the home page.
    """
    user = {"username": "Armin"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful in Portland"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool"},
    ]
    return render_template("home.html", title="Home", user=user, posts=posts)


@app.route("/about")
def about():
    """
    Render the 'about' page.

    Returns:
        Response: The HTML content for the 'about' page with the title 'About'.
    """
    return render_template("about.html", title="About")
