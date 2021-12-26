# 该类用于用户的取单词、提交单词等事件
# 面向对象是已经登录的用户
import random

import pymysql

from sql.sql_operator import Operator


# 继承Operator
class User(Operator):
    @classmethod
    def get_word_list(cls, id):
        table_name = "vocabulary_%s" % id

        # 新学20个单词，复习二十个单词
        sql = """
            (SELECT * FROM `%s` WHERE VALUE = 0 AND VALUE < 10 LIMIT 20)
            UNION
            (SELECT * FROM `%s` WHERE VALUE <> 0 AND VALUE < 10 LIMIT 10)
            """ % (table_name, table_name)

        cursor = cls.user_db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)  # 获取新学的单词
        result = cursor.fetchall()

        for i in result:  # 为其添加混淆项
            candidate = cls.get_candidate(id, i["ID"])
            i["Candidate"] = [{"id": i["ID"], "str": i["PARAPHRASE"]},
                              {"id": candidate[0]["ID"], "str": candidate[0]["PARAPHRASE"]},
                              {"id": candidate[1]["ID"], "str": candidate[1]["PARAPHRASE"]},
                              {"id": candidate[2]["ID"], "str": candidate[2]["PARAPHRASE"]}]
            random.shuffle(i["Candidate"])
        cursor.close()
        return result

    @classmethod
    def get_candidate(cls, user_id, correct_id):  # 取混淆项
        listName = "vocabulary_%s" % user_id
        sql = "SELECT ID, PARAPHRASE FROM %s WHERE ID <> %d LIMIT 3" % (listName, correct_id)
        cursor = cls.user_db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    @classmethod
    def set_value(cls, id_list, wrong_list, user_id):
        table_name = "vocabulary_%s" % user_id

        if len(id_list) != len(wrong_list):
            print("Error!")
            return False
        else:
            sql = ""
            for i in range(len(id_list)):
                print(wrong_list[i])
                if wrong_list[i] == 0:
                    sql = "UPDATE %s SET VALUE = VALUE + 2 WHERE ID = %d" % (table_name, id_list[i])
                else:
                    sql = "UPDATE %s SET VALUE = VALUE + %d WHERE ID = %d" % (table_name, wrong_list[i], id_list[i])
                cursor = cls.user_db.cursor(pymysql.cursors.DictCursor)
                cursor.execute(sql)
            cls.user_db.commit()
            cursor.close()
        return True
