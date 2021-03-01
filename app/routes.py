import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db, login
from app.forms import LoginFormUser, LoginFormOther, LoginForm, ItemForm
from flask_login import current_user, login_user, logout_user
from app.models import User, UserData, RequestedItem
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from flask_login import login_required

@login.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None


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
        user = User(
          username=userForm.username.data, 
          email=userForm.email.data)
        user.set_password(userForm.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=userForm.remember.data)
        return redirect(url_for('account'))

    if otherForm.submit2.data and otherForm.validate():
        store = User(
          username=otherForm.username.data,
          email=otherForm.email.data)
        store.set_password(otherForm.password.data)

        user_data = UserData(
          name=otherForm.name.data, state=otherForm.state.data,
          zip_code=otherForm.zip_code.data, 
          phone=otherForm.phone.data, 
          store_type=otherForm.storeType.data, 
          user=store)

        db.session.add(store)
        db.session.add(user_data)
        db.session.commit()
        login_user(store, remember=otherForm.remember.data)

        return redirect(url_for('account'))

    return render_template('signup.html', userForm=userForm, otherForm=otherForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    userForm = LoginForm()

    if userForm.validate_on_submit():
        user = User.query.filter_by(username=userForm.username.data).first()

        if user is None or not user.check_password(userForm.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

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

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    user = load_user(current_user.get_id())
    form = ItemForm()

    if form.validate_on_submit():
      f = form.photo.data
      filename = secure_filename(f.filename)
      f.save(os.path.join(
        app.instance_path, 'photos', filename
      ))

      requestedItem = RequestedItem(
        name=form.name.data,
        description=form.description.data,
        image=filename,
        price=form.price.data,
        quantity=form.quantity.data,
        user=user
      )
      db.session.add(requestedItem)
      db.session.commit()

      return redirect(url_for('account'))
      
    if user.user_data.store_type == 'Food Pantry':
      print(user.user_data.store_type)
      return render_template('pantry.html', user=user, itemForm=form)
    elif user.user_data.store_type == "Store":
      return render_template('store.html', user=user)
    else:
      return render_template('user.html', user=user)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/requestitem', methods=['POST'])
@login_required
def requestItem():
  user = load_user(current_user.get_id())
  form = itemForm()



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
