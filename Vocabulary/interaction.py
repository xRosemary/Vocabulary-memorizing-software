from Back_End.sql_initial import MyDatabase
from Back_End.sql_operator import Operator
from Back_End.extraction import Extraction


class Interaction:
    def __init__(self):
        username = ''
        password = ''
        DBName = ''

        MyDB = MyDatabase('localhost', username, password, DBName)
        DB_Operator = Operator(MyDB.db)
        extraction = Extraction(DB_Operator, "vocabulary")
        self.ans = extraction.extraction_word(30, 30, 30)

    def getlist(self):
        return list(self.ans), list(self.ans[:, 4])
