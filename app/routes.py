from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginFormUser, LoginFormOther, LoginForm

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  userForm = LoginFormUser()
  otherForm = LoginFormOther()

  if userForm.submit.data and userForm.validate():
    flash('Login request for user {}'.format(userForm.username.data))
    return redirect(url_for('account'))
  
  if otherForm.submit2.data and otherForm.validate():
    return redirect(url_for('account'))

  return render_template('signup.html', userForm = userForm, otherForm = otherForm)

@app.route('/login')
def login():
  userForm = LoginForm()
  return render_template('login.html', userForm=userForm)

@app.route('/account')
def account():
  return render_template('account.html')

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404