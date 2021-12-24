import pymysql
from Vocabulary.sql.sql_initial import MyDatabase


class Operator:
    """
    这个类主要用于操作数据库，包括增删改查
    """

    def __init__(self):
        username = "root"
        password = "123456"
        staticDBName = "static_db"
        userDBName = "user_db"
        self.db = MyDatabase('localhost', username, password, staticDBName).db
        self.user_db = MyDatabase('localhost', username, password, userDBName).db

    # 创建列表
    # def creatList(self, name):
    #     # 使用 cursor(pymysql.cursors.DictCursor) 方法创建一个游标对象 cursor
    #     cursor = self.user_db.cursor(pymysql.cursors.DictCursor)
    #
    #     try:
    #         # 使用 execute() 方法执行 SQL，如果表存在则删除
    #         cursor.execute("DROP TABLE IF EXISTS `%s`" % name)
    #
    #         # 使用预处理语句创建表
    #         sql = """CREATE TABLE `%s` (
    #                          ID INT NOT NULL,
    #                          WORD  CHAR(20) NOT NULL,
    #                          PRONOUNCE  CHAR(25),
    #                          PHONETIC  CHAR(255),
    #                          PARAPHRASE CHAR(255))
    #                          """ % name
    #         cursor.execute(sql)
    #
    #         # 提交到数据库执行
    #         self.user_db.commit()
    #     except Exception:
    #         # 如果发生错误则回滚
    #         self.user_db.rollback()
    #         print("Error: unable to create list")
    #     cursor.close()

    # 插入单词
    def insertWORD(self, name, _id, _word, _phonetic=None, _paraphrase=None, _pronounce=None, _value=0):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        sql = """INSERT INTO `%s`
                (ID, WORD, PRONOUNCE, PHONETIC, PARAPHRASE, VALUE) 
                 VALUES (%s, '%s', '%s', '%s', '%s', %s)
                 """ % (name, _id, _word, _pronounce, _phonetic, _paraphrase, _value)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to insert words：" +
                  str(_id) + _word + _pronounce + _paraphrase)
        cursor.close()

    # 按id查询单词
    def find_id(self, name, _id):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        # SQL 查询语句
        sql = "SELECT * FROM `%s` WHERE ID LIKE %d" % (name, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except Exception:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 按value取单词列表
    def find_value(self, name, mode):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.user_db.cursor(pymysql.cursors.DictCursor)

        # SQL 查询语句,分别为查询value大于、小于或等于0的单词
        if mode == -1:
            sql = "SELECT * FROM `%s` WHERE VALUE < 0" % name
        elif mode == 0:
            sql = "SELECT * FROM `%s` WHERE VALUE LIKE 0" % name
        elif mode == 1:
            sql = "SELECT * FROM `%s` WHERE VALUE > 0" % name
        else:
            print("Please enter the correct mode value")
            return None

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.user_db.commit()
            return results
        except Exception:
            self.user_db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 按字符查询单词
    def find_word(self, name, _word):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        # SQL 查询语句
        sql = "SELECT * FROM `%s` WHERE WORD LIKE '%s'" % (name, _word)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except Exception:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 查询全部单词
    def find_all(self, name):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        # SQL 查询语句
        sql = "SELECT * FROM `%s`" % name
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except Exception:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 删除表
    def deleteList(self, name):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        try:
            # 执行sql语句
            cursor.execute("DROP TABLE IF EXISTS `%s`" % name)
            # 提交到数据库执行
            self.db.commit()
        except Exception:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to delete list")
        cursor.close()

    # 删除单词
    def deleteWord(self, name, _id):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        # SQL 删除语句
        sql = "DELETE FROM `%s` WHERE ID = %d" % (name, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            self.db.commit()
        except Exception:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to delete word")
        cursor.close()

    # 按id取指定字段
    def get_filed(self, name, _id, filed):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        # SQL 查询语句
        sql = "SELECT `%s` FROM `%s` WHERE ID LIKE %d" % (filed, name, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except Exception:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 修改指定字段
    def set_filed(self, name, _id, filed, value):
        # 使用cursor(pymysql.cursors.DictCursor)方法获取操作游标
        cursor = self.db.cursor(pymysql.cursors.DictCursor)

        # SQL 修改语句
        sql = "UPDATE `%s` SET `%s` = '%s' WHERE ID = %d" % (name, filed, value, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            print("Error: unable to update field")
        cursor.close()

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

    # 创建账户并调用creatUserList方法
    def createUser(self, account, password, identity):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
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
                print("user's list has created")
            else:
                print("account is existed")
            self.db.commit()
        except Exception:
            self.db.rollback()
            print("Error: unable to create account")
        cursor.close()

    # 验证账户密码，若成功返回用户id，若不存在账户则返回-1，若密码错误则返回-2
    def identify(self, account, password, name="users"):
        # 初始化用户id，和身份
        id = -1
        identity = -1
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        # SQL 查询语句
        sql = "SELECT * FROM `%s` WHERE account LIKE '%s'" % (name, account)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results) == 0:
                # 用户不存在则返回-1
                id = -1
            else:
                if results[0]["password"] == password:
                    id = results[0]["id"]
                    identity = results[0]["identity"]
                else:  # 用户密码错误则返回-2
                    id = -2
            self.db.commit()
        except Exception:
            self.db.rollback()
            print("Error: unable to login")
        cursor.close()
        return id, identity

    # 关闭数据库
    def closeDB(self):
        self.db.close()
        self.user_db.close()
