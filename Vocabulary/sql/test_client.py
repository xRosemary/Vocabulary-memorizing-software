from Vocabulary.sql.sql_initial import MyDatabase
from Vocabulary.sql.sql_operator import Operator
from Vocabulary.sql.extraction import Extraction
from Vocabulary.sql.login import Login


if __name__ == "__main__":
    DB_Operator = Operator()

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
    print(DB_Operator.login("test","test"))
    # login = Login(DB_Operator, "users")
    # login.Register("abcq","123")
    DB_Operator.closeDB()
