from flask import Flask, render_template, url_for, request 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/account')
def account():
  return render_template('account.html')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
