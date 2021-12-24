from Vocabulary.sql.User import User


class Administrator(User):

    # 管理员创建账号
    def createAccount(self, op, new_account, new_password):
        op.createUser(new_account, new_password)

    # 管理员插入单词
    def insertWORD(self, op, name, _id, _word, _phonetic=None, _paraphrase=None, _pronounce=None, _value=0):
        op.insertWORD(name, _id, _word, _phonetic, _paraphrase, _pronounce, _value)

    # 按id查询单词
    def find_id(self, op, name, _id):
        return op.find_id(name, _id)

    # 按字符查询单词
    def find_word(self, op, name, _word):
        return op.find_word(name, _word)

    # 删除表
    def deleteList(self, op, name):
        op.deleteList(name)

    # 删除单词
    def deleteWord(self, op, name, _id):
        op.deleteWord(name, _id)

    # 按id取指定字段
    def get_filed(self, op, name, _id, filed):
        return op.get_filed(name, _id, filed)

    # 修改指定字段
    def set_filed(self, op, name, _id, filed, value):
        op.set_filed(name, _id, filed, value)
