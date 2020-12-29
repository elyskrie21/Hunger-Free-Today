from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo

class LoginFormUser(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField('Repeat Password')
  email = StringField('Email', validators=[DataRequired(), Email()])
  submit = SubmitField('Sign In')

class LoginFormFoodPantry(FlaskForm):
  pass

class LoginFormStore(FlaskForm):
  pass 