import numpy as np


class Extraction:
    """
    这个类主要用于取数据库中的单词
    """
    DB_Operator = object
    listName = ""

    def __init__(self, dbo, name):
        self.DB_Operator = dbo
        self.listName = name

    # 根据参数取出指定数量的单词
    def extraction_word(self, amount0=10, amount1=10, amount2=10): # 先写死
        # 取出value=0的单词
        arr0 = np.array(self.DB_Operator.find_value(self.listName, 0))
        # 取出value>0的单词
        arr1 = np.array(self.DB_Operator.find_value(self.listName, 1))
        # 取出value<0的单词
        arr2 = np.array(self.DB_Operator.find_value(self.listName, -1))

        try:
            # 尝试将取出来的单词列表按value排序
            if len(arr1) > 0:
                arr1 = arr1[np.lexsort(arr1.T)]
            if len(arr2) > 0:
                arr2 = arr2[np.lexsort(arr2.T)]
            # 按指定数量截取
            if amount0 < len(arr0): # 当数量充足时，去排序后的前amount个单词
                arr0 = arr0[:amount0]
            if amount1 < len(arr1):
                arr1 = arr1[:amount1]
            if amount2 < len(arr2):
                arr2 = arr2[len(arr2) - amount2:]
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
        # self.clipArray(ans)
        return ans

    # 裁剪数组，去掉id和value字段
    # @staticmethod
    # def clipArray(arr):
    #     try:
    #         if len(arr) != 0:
    #             arr = arr[:, : len(arr[0]) - 1]
    #     except:
    #         print("Error: unable to clip array")
    #     return arr
