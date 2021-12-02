import random

from flask import Blueprint, request, session

# from app import MyDatabase

reqAPI = Blueprint('reqAPI', __name__)


@reqAPI.route('/getNextWord', methods=["post"])
def getNextWord():
    # wordlist = session.get("wordlist")

    # word = wordlist.pop()
    WORD_ID = random.randint(1, 100)
    Candidate = [{"CN": "正确的答案", "ID": WORD_ID},
                 {"CN": "混淆1", "ID": random.randint(1, 100)},
                 {"CN": "混淆2", "ID": random.randint(1, 100)},
                 {"CN": "混淆3", "ID": random.randint(1, 100)}]  # 从数据库中抽取
    random.shuffle(Candidate)  # 打乱顺序

    item = {"WORD": random.choice('zyxwvutsrqponmlkjihgfedcba'),
            "WORD_ID": WORD_ID,
            "PRONOUNCE": "[sdfkjsd]",
            "PHONETIC": "https://",
            "Candidate": Candidate
            }
    return item


@reqAPI.route("/setWordList", methods=["post"])
def setWordList():
    wordlist = ["aaa0", "bbb0"]
    session["wordlist"] = wordlist

    return ""


@reqAPI.route("/getAnswer", methods=["post"])
def getAnswer():
    request.values.get("wordlist")
    pass

# （1）result = session[‘key’] ：如果内容不存在，将会报异常
# （2）result = session.get(‘key’) ：如果内容不存在，将返回None（推荐用法）
