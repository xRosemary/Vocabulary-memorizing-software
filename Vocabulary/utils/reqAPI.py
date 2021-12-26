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
    id_list: list = request.values.get("id_list")
    score_list: list = request.values.get("score_list")
    # 加吧

    return {}
