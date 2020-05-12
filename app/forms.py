from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired

csrf = CSRFProtect() 

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('Please enter your first name.')])
    last_name = StringField('Last Name', validators=[DataRequired('Please enter your last name.')])
    user_name = StringField('User Name', validators=[DataRequired('Please enter your user name.')])
    email = StringField('E-mail', validators=[DataRequired('Please enter your e-mail address.'), Email()])
    location = StringField('Location', validators=[DataRequired('Please enter your location.')])
    gender = SelectField('Gender', validators=[DataRequired('Please enter your gender.')], choices=[('',''),('Male', 'Male'),('Female','Female')])
    bio = TextAreaField('Bio', validators=[DataRequired('Please enter your bio.')])
    image =  FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Save')

class PostForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired('Please enter your user name.')])
    image =  FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    desc = TextAreaField('Description', validators=[DataRequired('Please enter your bio.')])
    submit = SubmitField('Save')
