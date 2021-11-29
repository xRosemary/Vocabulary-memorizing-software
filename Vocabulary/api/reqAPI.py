import random

from flask import Blueprint, request, session

reqAPI = Blueprint('reqAPI', __name__)


@reqAPI.route('/getNextWord', methods=["post"])
def getNextWord():
    wordlist = request.values.get("wordlist")

    wordlist = session.get("wordlist")
    if wordlist:
        word = wordlist.pop()
        word_id = 100
        word_right = random.randint(0, 3)
        word_Candidate = ["混淆1", "混淆2", "混淆3"]  # 从数据库中抽取
        word_Candidate.insert(word_right, "正确的意思")  # 从数据库中抽取

        session["wordlist"] = wordlist
    #  如果背完了 需要另外处理 暂时不写
    else:
        word = random.randint(0, 9)
        word_id = 100
        word_right = random.randint(0, 3)
        word_Candidate = ["混淆1", "混淆2", "混淆3"]  # 从数据库中抽取
        word_Candidate.insert(word_right, "正确的意思")  # 从数据库中抽取

    item = {"WORD": word,
            "WORD_ID": word_id,
            "PRONOUNCE": "[sdfkjsd]",
            "PHONETIC": "https://",
            "Candidate": word_Candidate,
            "word_right": word_right
            }

    session["currentWord"] = item
    return item


@reqAPI.route("/setWordList", methods=["post"])
def setWordList():
    wordlist = request.values.get("wordlist").split("\n")
    session["wordlist"] = wordlist
    return ""

@reqAPI.route("/getAnswer", methods=["post"])
def getAnswer():
    request.values.get("wordlist")
    pass


# （1）result = session[‘key’] ：如果内容不存在，将会报异常
# （2）result = session.get(‘key’) ：如果内容不存在，将返回None（推荐用法）
