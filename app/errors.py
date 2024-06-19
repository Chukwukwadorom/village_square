from flask import render_template
from sqlalchemy.exc import IntegrityError
from app import app, db


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
@app.errorhandler(IntegrityError)
def internal_error(error):
    print("error 500 here")
    db.session.rollback()

    return render_template("500.html"), 500