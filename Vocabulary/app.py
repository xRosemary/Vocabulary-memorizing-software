from flask import Flask, render_template
import os
from utils.reqAPI import reqAPI

# from utils.sql.sql_initial import *
# from utils.sql.sql_operator import *
# from utils.sql.extraction import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(reqAPI, url_prefix='/req')

# MyDB = MyDatabase('localhost', "root", "123456", "Project1")
# DB_Operator = Operator(MyDB.db)
# extraction = Extraction(DB_Operator, "testlist")


@app.route('/')
def reIndex():
    return render_template('newindex.html')


@app.route('/learn')
def reLearn():
    return render_template('newlearn.html')


if __name__ == '__main__':
    app.run()
