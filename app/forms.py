from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


if __name__ == "__main__":
    import os
    print(__name__)
    print(__file__)
    print(os.path.dirname(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))