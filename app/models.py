from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(120))

  def __repr__(self):
    return '<User {}>'.formate(self.username)

class Store(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  name = db.Column(db.String(120), index=True)
  storeType = db.column(db.String(64), index=True)
  phone = db.Column(db.String(64), index=True, unique=True)
  state = db.Column(db.Stirng(64), index=True)
  zip_code = db.column(db.Integer, index=True)
  password_hash = db.Column(db.String(120))

  def __repr__(self):
    return '<User {}>'.format(self.username)