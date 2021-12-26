# 该类用于用户的取单词、提交单词等事件
# 面向对象是已经登录的用户

import pymysql
import random
from sql.sql_operator import Operator


# 继承Operator
class User(Operator):
    @classmethod
    def get_word_list(cls, id):
        listName = "vocabulary_%s" % id
        sql1 = "SELECT * FROM %s WHERE VALUE = 0 LIMIT 10" % listName
        cursor = cls.user_db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql1)
        result = cursor.fetchall()
        for i in result:
            Candidate = [{"id": i["ID"], "str": i["PARAPHRASE"]}, {"id": 666, "str": "混淆A"}, {"id": 777, "str": "混淆B"}, {"id": 888, "str": "混淆C"}]
            random.shuffle(Candidate)
            i["Candidate"] = Candidate
        cursor.close()
        return result

# print(User.get_word_list(8))
