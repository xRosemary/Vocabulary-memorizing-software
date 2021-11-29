from flask import Flask, render_template, session, request
import config
import os
from api.reqAPI import reqAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(reqAPI, url_prefix='/req')


@app.route('/')
def reIndex():
    return render_template('index.html')


@app.route('/learn')
def reLearn():
    return render_template('learn.html')


if __name__ == '__main__':
    app.run()
