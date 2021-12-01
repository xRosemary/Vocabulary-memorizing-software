from Back_End.sql_initial import MyDatabase
from Back_End.sql_operator import Operator
from Back_End.extraction import Extraction

if __name__ == "__main__":
    username = "root"
    password = "123456"
    DBName = "static_db"

    MyDB = MyDatabase('localhost', username, password, DBName)
    UserDB = MyDatabase('localhost', username, password, "user_db")
    DB_Operator = Operator(MyDB.db,UserDB.db)
    # extraction = Extraction(DB_Operator, "vocabulary_1")
    """
    数据库操作例子
    DB_Operator.insertWORD("testlist", 1, "aaa")
    DB_Operator.creatList("testlist")
    DB_Operator.deleteList("testlist")
    print(DB_Operator.find_id("testlist", 2))
    print(DB_Operator.find_word("testlist", 'aaa'))
    print(DB_Operator.find_all("testlist"))
    print(DB_Operator.get_filed("testlist", 2, "word"))
    DB_Operator.deleteWord("testlist", 1)
    DB_Operator.set_filed("testlist", 2, "WORD", "bbb")
    """
    # print(DB_Operator.find_all("vocabulary"))
    # print(DB_Operator.find_value("testlist", 1))
    # ans = extraction.extraction_word()
    # ans = extraction.clipArray(ans)
    # print(ans)
    # DB_Operator.creatUserList(1)
    DB_Operator.closeDB()
