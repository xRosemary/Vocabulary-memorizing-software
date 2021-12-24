from Vocabulary.sql.User import User
import numpy as np


class CommonUser(User):

    def __init__(self):
        super().__init__()

    # 根据id取出混淆项的中文
    def getCandidate(self, op, id_set):
        Candidate_Word = []
        for i in id_set:
            p = op.get_filed(name="vocabulary_total", _id=i, filed="PARAPHRASE")
            Candidate_Word.append(p[0]["PARAPHRASE"])
        return Candidate_Word

    # 根据参数取出指定数量的单词
    def extraction_word(self, op, amount0=20, amount1=5, amount2=5):  # 先写死

        listName = "vocabulary_" + str(super.user_id)
        # 取出value=0的单词
        arr0 = np.array(op.find_value(listName, 0))
        # 取出value>0的单词
        arr1 = np.array(op.find_value(listName, 1))
        # 取出value<0的单词
        arr2 = np.array(op.find_value(listName, -1))

        try:
            # 尝试将取出来的单词列表按value排序
            if len(arr1) > 0:
                # sorted(列表，key = lambda 形参：形参[str键名称])
                arr1 = sorted(arr1, key=lambda word: word["VALUE"])
            if len(arr2) > 0:
                arr2 = sorted(arr2, key=lambda word: word["VALUE"])

            # 按指定数量截取
            if amount0 < len(arr0):  # 当数量充足时，去排序后的前amount个单词
                arr0 = arr0[:amount0]
            if amount1 < len(arr1):
                arr1 = arr1[:amount1]
            if amount2 < len(arr2):
                arr2 = arr2[:amount2]
        except Exception:
            print("Error: unable to get word list")

        # 合并三个数组，并返回
        ans = np.empty(0)
        try:
            if len(arr2) > 0:
                ans = np.append(ans, arr2, axis=0)
            if len(arr0) > 0:
                ans = np.append(ans, arr0, axis=0)
            if len(arr1) > 0:
                ans = np.append(ans, arr1, axis=0)
        except Exception:
            print("Error: unable to combine arrays")
        return list(ans)
