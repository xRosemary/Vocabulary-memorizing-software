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
    def extraction_word(self, amount0, amount1, amount2):
        # 取出value=0的单词
        arr0 = np.array(self.DB_Operator.find_value(self.listName, 0))

        # 取出value>0的单词，并按照value排序
        arr1 = np.array(self.DB_Operator.find_value(self.listName, 1))
        arr1 = arr1[np.lexsort(arr1.T)]

        # 取出value<0的单词，并按照value排序
        arr2 = np.array(self.DB_Operator.find_value(self.listName, -1))
        arr2 = arr2[np.lexsort(arr2.T)]

        # 取指定数量
        if amount0 < len(arr0):
            arr0 = arr0[:amount0]
        if amount1 < len(arr1):
            arr1 = arr1[:amount1]
        if amount2 < len(arr2):
            arr2 = arr2[:amount2]

        # 合并三个数组，并返回
        return np.concatenate([arr2, arr0, arr1])

    # 裁剪数组，去掉id和value字段
    @staticmethod
    def clipArray(arr):
        return arr[:, 1: len(arr[0]) - 1]