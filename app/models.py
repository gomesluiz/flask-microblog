from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app import login


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


class User(UserMixin, db.Model):
    """
    User model for storing user details.

    Attributes:
        id (int): Primary key.
        username (str): Unique username.
        email (str): Unique email address.
        password_hash (str): Hashed password.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped["Post"] = so.relationship(back_populates="author")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    """
    Represents a blog post in the database.
    Attributes:
        id (int): The unique identifier for the post.
        body (str): The content of the post, limited to 140 characters.
        timestamp (str): The time when the post was created, indexed for quick lookup.
        user_id (int): The ID of the user who authored the post, indexed for quick lookup.
        author (User): The user who authored the post, establishing a relationship with the User model.
    Methods:
        __repr__(): Returns a string representation of the Post instance.
    """

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[str] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)

    author: so.Mapped[User] = so.relationship(back_populates="posts")

    def __repr__(self):
        return f"<Post {self.body}>"
