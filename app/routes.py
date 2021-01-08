from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginFormUser, LoginFormOther, LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Store 
from werkzeug.urls import url_parse
from flask_login import login_required

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('account'))

  userForm = LoginFormUser()
  otherForm = LoginFormOther()

  if userForm.submit.data and userForm.validate():
    user = User(username=userForm.username.data, email=userForm.email.data)
    user.set_password(userForm.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=userForm.remember.data)
    return redirect(url_for('account'))
  
  if otherForm.submit2.data and otherForm.validate():
    store = Store(username=otherForm.username.data, email=otherForm.email.data, name=otherForm.name.data, state=otherForm.state.data, zip_code=otherForm.zip_code.data,phone=otherForm.phone.data, store_type=otherForm.storeType.data)
    store.set_password(otherForm.password.data)
    db.session.add(store)
    db.session.commit()
    login_user(store, remember=otherForm.remember.data)
    return redirect(url_for('account'))

  return render_template('signup.html', userForm = userForm, otherForm = otherForm)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('account'))

  userForm = LoginForm()
  
  if userForm.validate_on_submit():
    user = User.query.filter_by(username=userForm.username.data).first()
    store = Store.query.filter_by(username=userForm.username.data).first()
    
    if user is None or not user.check_password(userForm.password.data):
      if store is None or not store.check_password(userForm.password.data):
        flash('Invalid username or password')
        return redirect(url_for('login'))
      else:
        login_user(store, remember=userForm.remember.data)
    else:
      login_user(user, remember=userForm.remember.data)
    
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(url_for('account'))

  return render_template('login.html', userForm=userForm)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route('/account')
@login_required
def account():
  return render_template('account.html')

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404