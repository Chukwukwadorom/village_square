from app import db, login
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as sa_o
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



# class User(db.Model):
#     id: sa_o.Mapped[int] = sa_o.mapped_column(primary_key=True)
#     username: sa_o.Mapped[str] = sa_o.mapped_column(sa.String(64), index=True, unique=True)
#     email: sa_o.Mapped[str] = sa_o.mapped_column(sa.String(128), index= True, unique=True)
#     password_hash: sa_o.Mapped[Optional[str]] = sa_o.mapped_column(sa.String(256))

#     posts: sa_o.WriteOnlyMapped["Post"] = sa_o.relationship(back_populates="author")

#     def __repr__(self):
#         return '<User {}>'.format(self.username)
    
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

@login.user_loader
def user_loader(id):
    return db.session.get(User, int(id))
    
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    posts = db.relationship('Post', back_populates='author')

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id:sa_o.Mapped[int] = sa_o.mapped_column(primary_key=True)
    body:sa_o.Mapped[str] = sa_o.mapped_column(sa.String(160))
    timestamp:sa_o.Mapped[datetime] = sa_o.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: sa_o.Mapped[int] =sa_o.mapped_column(sa.ForeignKey(User.id), index=True)
    author: sa_o.Mapped[User] = sa_o.relationship(back_populates="posts")

    def __repr__(self):
        return '<Post {}>'.format(self.body)
