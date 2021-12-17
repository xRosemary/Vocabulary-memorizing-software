from Vocabulary.sql.sql_operator import Operator
from Vocabulary.sql.extraction import Extraction


class Convey:
    def __init__(self):
        self.DB_Operator = Operator()

    def getData(self, userID):
        extraction = Extraction(self.DB_Operator, "vocabulary_" + str(userID))
        ans = extraction.extraction_word()
        return list(ans)
