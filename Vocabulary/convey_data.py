from Vocabulary.utils.sql.sql_initial import MyDatabase
from Vocabulary.utils.sql.sql_operator import Operator
from Vocabulary.utils.sql.extraction import Extraction


class Convey:
    def __init__(self):
        username = "root"
        password = "xym981120"
        staticDBName = "static_db"
        userDBName = "user_db"
        MyDB = MyDatabase('localhost', username, password, staticDBName)
        UserDB = MyDatabase('localhost', username, password, userDBName)
        self.DB_Operator = Operator(MyDB.db, UserDB.db)

    def getData(self, userID):
        extraction = Extraction(self.DB_Operator, "vocabulary_" + str(userID))
        ans = extraction.extraction_word()
        return list(ans)
