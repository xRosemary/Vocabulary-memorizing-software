import pymysql


def connectMySql(host, user, password, database):
    db = pymysql.connect(host=host, user=user, password=password, database=database)
    # db = pymysql.connect(host=host, user=user, password=password, charset='utf8')
    # cur = db.cursor()
    # sql = "create database [if not exists] %s character set utf8mb4 COLLATE utf8mb4_general_ci;" % database
    # cur.execute(sql)
    # path = database + ".sql"
    # execute_fromfile(path, cur)
    return db


def execute_fromfile(filename, cursor):  # 封装一个读取sql文件中的sql语句，并执行语句的方法
    fd = open(filename, 'r', encoding='utf-8')  # 以只读的方式打开sql文件
    sqlFile = fd.read()  # 读取文件内容
    fd.close()
    sqlCommamds = sqlFile.split(';')  # 以;切割文件内容，获取单个sql语句

    for command in sqlCommamds:
        try:
            cursor.execute(command)
        except Exception as msg:
            print("错误信息： ", msg)

    print('sql执行完成')
