import pymysql


class MyDatabase:
    db = pymysql.Connect

    def __init__(self, host, user, password, database):
        self.db = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database)



