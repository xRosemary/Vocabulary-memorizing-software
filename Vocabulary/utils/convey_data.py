from Vocabulary.sql.sql_operator import Operator
from Vocabulary.sql.extraction import Extraction


class Convey:
    def __init__(self):
        self.DB_Operator = Operator()

    def getData(self, userID):
        extraction = Extraction(self.DB_Operator, "vocabulary_" + str(userID))
        ans = extraction.extraction_word()
        return list(ans)
    
    def getCandidate(self, id_set):
        # 根据id取出混淆项的中文
        Candidate_Word = []
        for i in id_set:
            p = self.DB_Operator.get_filed(name="vocabulary_total", _id=i, filed="PARAPHRASE")
            Candidate_Word.append(p[0]["PARAPHRASE"])
        return Candidate_Word
