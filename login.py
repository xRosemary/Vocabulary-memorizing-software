from Vocabulary.sql.Administrator import Administrator
from Vocabulary.sql.CommonUser import CommonUser


def login(op, account, password):
    user_id, identity = op.identify(account, password)
    if user_id >= 0:
        if identity == 1:
            return Administrator(user_id, account, password)
        else:
            return CommonUser(user_id, account, password)
    else:
        return None
