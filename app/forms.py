from flask_wtf import FlaskForm
from flask_wtf.file import *
from wtforms import StringField, PasswordField, TextAreaField, RadioField,FileField,SubmitField
from wtforms.validators import InputRequired, NumberRange, Required, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[Required()])
    lname = StringField('Last Name', validators=[Required()])
    location = StringField('Location', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    sex=RadioField('Sex', choices=[('Male','Male'),('Female','Female')])
    bio= TextAreaField('Biography', validators=[Required()])
    photo= FileField('Profile Image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])
    submit = SubmitField('Submit')
