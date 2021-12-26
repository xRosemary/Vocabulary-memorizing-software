from flask import Flask, render_template
import os
from utils.login import loginAPI
from utils.reqAPI import reqAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(loginAPI, url_prefix='/login')
app.register_blueprint(reqAPI, url_prefix='/req')


@app.route('/')
def login_html():
    return render_template('login.html')


@app.route('/index')
def index_html():
    return render_template('newindex.html')


@app.route('/learn')
def learn_html():
    return render_template('newlearn.html')


@app.route('/signup')
def signup_html():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
