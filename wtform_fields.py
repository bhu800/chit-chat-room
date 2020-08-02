from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ Registration Form """
    username = StringField('username_label', validators=[InputRequired(message="Username Required!"),
        Length(min=3, max=27, message="Username must be in between 3 to 27 characters.")])
    password = PasswordField("password_label", validators=[InputRequired(message="Password Required!"),
        Length(min=6, max=27, message="Password must be in between 6 to 27 characters.")])
    confirm_password = PasswordField("confirm_password_label", validators=[InputRequired(message="Password Required!"), 
        EqualTo("password", message="Passwords must match!")])
    submit_button = SubmitField("SignUp!")