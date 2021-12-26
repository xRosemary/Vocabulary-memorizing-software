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
    # 分割文本
    id_list = request.values.get("id_list").strip('[]').split(',')
    score_list = request.values.get("score_list").strip('[]').split(',')

    # 转换数据类型
    id_list = [int(x) for x in id_list]
    score_list = [int(x) for x in score_list]
    User.set_value(id_list, score_list, user_id)

    return {}
