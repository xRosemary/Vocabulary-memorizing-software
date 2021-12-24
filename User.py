class User:
    def __init__(self, user_id, account, password):
        self.user_id = user_id
        self.account = account
        self.password = password

    def get_all_list(self, op):
        return op.find_all()
