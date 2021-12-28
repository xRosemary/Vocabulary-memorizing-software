from flask import Blueprint, request, session
from sql.sql_user import User

reqAPI = Blueprint('reqAPI', __name__)


@reqAPI.route('/getWordList', methods=["post"])
def getWordList():
    user_id = session["id"]
    result = User.get_word_list(user_id)
    info = {"state": 1, "result": result, "total": len(result)}
    return info


@reqAPI.route('/summitScore', methods=["post"])
def summitScore():
    user_id = session["id"]
    id_list: list = request.form.getlist("id_list[]", type=int)
    score_list: list = request.form.getlist("score_list[]", type=int)
    User.set_value(id_list, score_list, user_id)
    return {}


