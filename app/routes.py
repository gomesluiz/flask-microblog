from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user
from urllib.parse import urlsplit
import sqlalchemy as sa

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Render the login page with the login form.

    Returns:
        Response: The HTML content for the login page with the title 'Sign In'.
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("home")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Render the registration page with the registration form.

    Returns:
        Response: The HTML content for the registration page with the title 'Register'.
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


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
