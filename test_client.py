from com.SoftwareEngineering.sql_initial import MyDatabase
from com.SoftwareEngineering.sql_operator import Operator
from com.SoftwareEngineering.extraction import Extraction

if __name__ == "__main__":
    username = ''
    password = ''
    listName = ''
    MyDB = MyDatabase('localhost', username, password, listName)
    DB_Operator = Operator(MyDB.db)
    extraction = Extraction(DB_Operator, "testlist")
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
    ans = extraction.extraction_word(1,4,2)
    ans = extraction.clipArray(ans)
    print(ans)
    DB_Operator.closeDB()
