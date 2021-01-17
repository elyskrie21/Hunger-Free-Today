from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DecimalField, FileField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
import phonenumbers
import re 
from app.models import User 

states = ["State","Alabama","Alaska","Arizona","Arkansas","California","Colorado",
          "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
          "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
          "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
          "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
          "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
          "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
          "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"
          ]

def validate_phone(form, field):
  if len(field.data) > 16:
    raise ValidationError('Invalid phone number')
    
  try:
    input_number = phonenumbers.parse(field.data)
    if not (phonenumbers.is_valid_number(input_number)):
      raise ValidationError('Invalid phone number')
  except:
    input_number = phonenumbers.parse('+1'+field.data)
    if not (phonenumbers.is_valid_number(input_number)):
      raise ValidationError('Invalid phone number')     
  
def validate_zip(form, field):
  print('hi')
  if re.match(r"^[0-9]{5}(?:-[0-9]{4})?$", field.data) is None:
    raise ValidationError('Invalid zip code')

def validate_username(form, field):
  user = User.query.filter_by(username=field.data).first()
  if user is not None:
    raise ValidationError('Username is taken, please use a different username')

def validate_email(form, field):
  user = User.query.filter_by(email=field.data).first()
  if user is not None:
    raise ValidationError("Email is already in use, please use a different email")

class LoginFormUser(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), validate_username])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField('Repeat Password', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email(), validate_email])
  remember = BooleanField()
  submit = SubmitField('Sign In')

class LoginFormOther(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), validate_username])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField('Repeat Password', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email(), validate_username])
  name = StringField('Food Pantry Name', validators=[DataRequired()])
  state = SelectField(label='State', choices = states, validators=[DataRequired()])
  zip_code = StringField('Zip', validators=[DataRequired(), validate_zip])
  phone = StringField('Phone', validators= [DataRequired(), validate_phone])
  storeType = SelectField(choices = ['Store or Food Pantry?', 'Store', 'Food Pantry'], validators=[DataRequired()])
  remember = BooleanField()

  submit2 = SubmitField('Sign In')

  def validate_state(form,field):
    if field.data == 'State':
      raise ValidationError('Please choose a state')

  def validate_storeType(form, field):
    if field.data == 'Store or Food Pantry?':
      raise ValidationError("Please choose Store or Food Pantry")

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField()

  submit = SubmitField('Sign In')

class ItemForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  description = StringField('Description', validators=[DataRequired()])
  price = DecimalField('Price', places=2, validators=[DataRequired()])
  image = FileField('Image File')
  quantity = StringField()
