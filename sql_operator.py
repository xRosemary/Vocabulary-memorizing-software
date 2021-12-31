from sql.sql_initial import connectMySql


class Operator:
    username = "root"
    password = "123456"
    staticDBName = "static_db"
    userDBName = "user_db"
    db = connectMySql('localhost', username, password, staticDBName)
    user_db = connectMySql('localhost', username, password, userDBName)
