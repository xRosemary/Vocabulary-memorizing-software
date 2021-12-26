import pymysql


def connectMySql(host, user, password, database):
    db = pymysql.connect(host=host, user=user, password=password, database=database)
    return db
