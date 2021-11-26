import pymysql


class Operator:
    """
    这个类主要用于操作数据库，包括增删改查
    """
    db = pymysql.Connect

    def __init__(self, db):
        self.db = db

    # 创建列表
    def creatList(self, name):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()

        try:
            # 使用 execute() 方法执行 SQL，如果表存在则删除
            cursor.execute("DROP TABLE IF EXISTS `%s`" % name)

            # 使用预处理语句创建表
            sql = """CREATE TABLE `%s` (
                             ID INT NOT NULL,
                             WORD  CHAR(20) NOT NULL,
                             PRONOUNCE  CHAR(25),
                             PHONETIC  CHAR(255),
                             PARAPHRASE CHAR(255),
                             VALUE INT default 0)
                             """ % name
            cursor.execute(sql)

            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to create list")
        cursor.close()

    # 插入单词
    def insertWORD(self, name, _id, _word, _phonetic=None, _paraphrase=None, _pronounce=None, _value=0):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        sql = """INSERT INTO `%s`
                (ID, WORD, PRONOUNCE, PHONETIC, PARAPHRASE, VALUE) 
                 VALUES (%s, '%s', '%s', '%s', '%s', %s)
                 """ % (name, _id, _word, _pronounce, _phonetic, _paraphrase, _value)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to insert words：" +
                  str(_id) + _word + _pronounce + _paraphrase)
        cursor.close()

    # 按id查询单词
    def find_id(self, name, _id):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM `%s` WHERE ID LIKE %d" % (name, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 按value取单词列表
    def find_value(self, name, mode):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

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
            self.db.commit()
            return results
        except:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 按字符查询单词
    def find_word(self, name, _word):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM `%s` WHERE WORD LIKE '%s'" % (name, _word)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 查询全部单词
    def find_all(self, name):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM `%s`" % name
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 删除表
    def deleteList(self, name):
        cursor = self.db.cursor()
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        try:
            # 执行sql语句
            cursor.execute("DROP TABLE IF EXISTS `%s`" % name)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to delete list")
        cursor.close()

    # 删除单词
    def deleteWord(self, name, _id):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 删除语句
        sql = "DELETE FROM `%s` WHERE ID = %d" % (name, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            print("Error: unable to delete word")
        cursor.close()

    # 按id取指定字段
    def get_filed(self, name, _id, filed):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 查询语句
        sql = "SELECT `%s` FROM `%s` WHERE ID LIKE %d" % (filed, name, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            self.db.commit()
            return results
        except:
            self.db.rollback()
            print("Error: unable to fetch words")
        cursor.close()

    # 修改指定字段
    def set_filed(self, name, _id, filed, value):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        # SQL 修改语句
        sql = "UPDATE `%s` SET `%s` = '%s' WHERE ID = %d" % (name, filed, value, _id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("Error: unable to update field")
        cursor.close()

    # 关闭数据库
    def closeDB(self):
        self.db.close()
