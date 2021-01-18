from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext import declarative

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    user_data = db.relationship('UserData', backref='user', uselist=False)
    requested_items = db.relationship('RequestedItem', backref='user')
    bought_items = db.relationship('BoughtItem', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# This model will connected to the user, store, and pantry
class UserData(db.Model):
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    store_type = db.Column(db.String(64), index=True)
    phone = db.Column(db.String(64), index=True, unique=True)
    state = db.Column(db.String(64), index=True)
    zip_code = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class RequestedItem(db.Model):
    __tablename__ = 'requested_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    description = db.Column(db.String, index=True)
    image = db.Column(db.String, index=True)
    price = db.Column(db.Numeric(10, 2), index=True)
    quantity = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Item {}>'.format(self.name)


class BoughtItem(db.Model):
    __tablename__ = 'bought_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    price = db.Column(db.Integer, index=True)
    quantity = db.Column(db.Integer, index=True)
    food_pantry = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Item {}>'.format(self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
