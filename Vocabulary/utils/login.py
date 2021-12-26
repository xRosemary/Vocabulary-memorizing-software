from flask import Blueprint, request, session
from sql.sql_login import sql_login

loginAPI = Blueprint('loginAPI', __name__)


@loginAPI.route('/', methods=["post"])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    user_info = sql_login.identify(username, password)
    session["id"] = user_info["id"]
    message = {"state": -1}
    if user_info["id"] > 0:
        message["state"] = 1
    return message


@loginAPI.route('/signup', methods=["post"])
def signup():
    username = request.values.get("username")
    password = request.values.get("password")
    return {"state": 1}
