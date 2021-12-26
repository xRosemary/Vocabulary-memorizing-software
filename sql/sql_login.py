# 该类用于处理与登录、注册有关的事件
# 面向的对象是游客未登录状态

import pymysql

from sql.sql_operator import Operator


class sql_login(Operator):
    # 权限原则上放在服务器存储

    # 不能继承self
    @classmethod
    def identify(cls, account, password, name="users"):
        # 初始化用户id，和身份
        user_info = {"id": -1, "identity": -1}
        cursor = cls.db.cursor(pymysql.cursors.DictCursor)
        # SQL 查询语句
        sql = "SELECT * FROM `%s` WHERE account LIKE '%s'" % (name, account)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results) == 0:
                user_info["id"] = -1
            else:
                if results[0]["password"] == password:
                    user_info["id"] = results[0]["id"]
                    user_info["identity"] = results[0]["identity"]
                else:  # 用户密码错误则返回-2
                    user_info["id"] = -2
            cls.db.commit()
        except Exception:
            cls.db.rollback()
            print("Error: unable to login")
        cursor.close()
        return user_info

    # 创建账户并调用creatUserList方法
    def createUser(self, account, password, identity=0):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        info = {"state": -1}
        # SQL 查询语句
        sql = "SELECT id FROM users WHERE account LIKE '%s'" % account
        sql_2 = """INSERT INTO users
                (account, password, identity) 
                 VALUES ('%s', '%s', %d)
                 """ % (account, password, identity)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results) == 0:
                cursor.execute(sql_2)
                print("created")
                # 获取所创建账户的id,并根据id创建一个表
                cursor.execute(sql)
                results = cursor.fetchall()
                self.db.commit()
                self.creatUserList(results[0]["id"])
                info["state"] = 1
                print("user's list has created")
            else:
                info["state"] = -2
            self.db.commit()
        except Exception:
            self.db.rollback()
            info["state"] = -3
            return info

        cursor.close()
        return info

    # 根据用户id创建用户表
    def creatUserList(self, id):
        cursor = self.user_db.cursor(pymysql.cursors.DictCursor)
        sql_1 = """CREATE TABLE IF NOT EXISTS vocabulary_%d (
                                     ID INT NOT NULL,
                                     WORD  CHAR(20) NOT NULL,
                                     PRONOUNCE  CHAR(25),
                                     PHONETIC  CHAR(255),
                                     PARAPHRASE CHAR(255))
                                     """ % id

        sql_2 = "insert into vocabulary_%d select * from static_db.vocabulary_total" % id
        sql_3 = "ALTER TABLE vocabulary_%d ADD VALUE INT default 0" % id
        try:
            cursor.execute(sql_1)
            cursor.execute(sql_2)
            cursor.execute(sql_3)
            self.user_db.commit()
        except Exception:
            self.user_db.rollback()
            print("Error: unable to create userList")
        cursor.close()


a = sql_login()
print(a.identify("hjh", "123456"))
# print(a.createUser("bbb", "123456"))
