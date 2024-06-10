from app import db
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as sa_o
from datetime import datetime, timezone


class User(db.Model):
    id: sa_o.Mapped[int] = sa_o.mapped_column(primary_key=True)
    username: sa_o.Mapped[str] = sa_o.mapped_column(sa.String(64), index=True, unique=True)
    email: sa_o.Mapped[str] = sa_o.mapped_column(sa.String(128), index= True, unique=True)
    password_hash: sa_o.Mapped[Optional[str]] = sa_o.mapped_column(sa.String(256))

    posts: sa_o.WriteOnlyMapped["Post"] = sa_o.relationship(back_populates="author")

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Post(db.Model):
    id:sa_o.Mapped[int] = sa_o.mapped_column(primary_key=True)
    body:sa_o.Mapped[str] = sa_o.mapped_column(sa.String(160))
    timestamp:sa_o.Mapped[datetime] = sa_o.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: sa_o.Mapped[int] =sa_o.mapped_column(sa.ForeignKey(User.id), index=True)
    author: sa_o.Mapped[User] = sa_o.relationship(back_populates="posts")

    def __repr__(self):
        return '<Post {}>'.format(self.body)
