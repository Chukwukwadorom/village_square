from app import app, db
import sqlalchemy as sa
import sqlalchemy.orm as sa_o
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'sa_o': sa_o, 'dbdb': db, 'User': User, 'Post': Post}