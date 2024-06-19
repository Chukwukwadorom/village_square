from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import PasswordField, StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")



class RegistrationForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    password2 = PasswordField("Repeat Password",validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up!")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError(f"{username.data} is not available, use a different username")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError(f"{email.data} is not available, use a different email")
        

class EditProfileForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    about_me = TextAreaField("About Me",validators=[DataRequired(), Length(min=0, max=150)])
    submit = SubmitField("Submit")

    def __init__(self, original_username,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username 

    def validate_username(self,username):
        if username.data != self.original_username:
           user = User.query.filter_by(username=username.data).first()
           if user:
            raise ValidationError(f"{username.data} is not available, use a different username")
        





if __name__ == "__main__":
    import os
    print(__name__)
    print(__file__)
    print(os.path.dirname(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))