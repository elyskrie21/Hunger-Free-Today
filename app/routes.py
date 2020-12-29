from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginFormUser

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  userForm = LoginFormUser()

  if userForm.validate_on_submit():
    flash('Login request for user {}'.format(userForm.username.data))
    return redirect(url_for('account'))

  return render_template('signup.html', userForm = userForm)
  

@app.route('/account')
def account():
  return render_template('account.html')

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404