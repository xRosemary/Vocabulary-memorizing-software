import pymysql


class MyDatabase:
    """
    这个类主要用于数据库的初始化
    """
    db = pymysql.Connect

    def __init__(self, host, user, password, database):
        self.db = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database)



