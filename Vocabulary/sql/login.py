class Login:

    def __init__(self, dbo, name):
        self.DB_Operator = dbo
        self.listName = name

    def Register(self, username, password):
        # # 调用hashlib里的方法，生成哈希值
        # md5 = hashlib.md5()
        # # 这个属于'加盐'，就是让哈希值更复杂，不易破解
        # md5.update(password + 'wpy' + username)
        # md = md5.hexdigest()+

        # # 生成哈希值
        # realpassword = md
        # # insert进数据库

        self.DB_Operator.createAccount(username, password)

    def UserLogin(self, username, password):
        # # 调用hashlib里的方法，生成哈希值
        # md5 = hashlib.md5()
        # # 这个属于'加盐'，就是让哈希值更复杂，不易破解
        # md5.update(password + 'wpy' + username)
        # md = md5.hexdigest()
        # # 生成哈希值
        # realpassword = md
        # # insert进数据库

        self.DB_Operator.createAccount(username, password)
