import random

from flask import Blueprint, request, session

# from app import MyDatabase
from Vocabulary.utils.convey_data import Convey
reqAPI = Blueprint('reqAPI', __name__)
convey = Convey()
wordlist = convey.getData(1)

@reqAPI.route('/getNextWord', methods=["post"])
def getNextWord():
    # wordlist = session.get("wordlist")

    word = wordlist.pop()
    WORD_ID = word["ID"]

    # 取出三个不等于该单词id的整数
    Candidate_Set = set()
    while len(Candidate_Set) < 3:
        i = random.randint(0, len(wordlist)-1)
        if i != WORD_ID:
            Candidate_Set.add(i)

    # 根据id取出混淆项的中文
    Candidate_Word = []
    for i in Candidate_Set:
        Candidate_Word.append(wordlist[i]["PARAPHRASE"])

    # 将混淆项与所背单词组合
    Candidate = [{"CN": word["PARAPHRASE"], "ID": WORD_ID},
                 {"CN": Candidate_Word[0], "ID": Candidate_Set.pop()},
                 {"CN": Candidate_Word[1], "ID": Candidate_Set.pop()},
                 {"CN": Candidate_Word[2], "ID": Candidate_Set.pop()}]  # 从数据库中抽取
    random.shuffle(Candidate)  # 打乱顺序

    item = {"WORD": word["WORD"],
            "WORD_ID": WORD_ID,
            "PRONOUNCE": word["PRONOUNCE"],
            "PHONETIC": word["PHONETIC"],
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
