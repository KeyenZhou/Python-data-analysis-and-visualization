# -*- coding: utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd


def create_dataframe():
    """
    返回值:
    df1: 一个DataFrame类型数据
    """
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    df1 = pd.DataFrame(columns=['states', 'years', 'pops'], index=['one', 'two', 'three', 'four', 'five'])
    df1['new_add'] = [7, 4, 5, 8, 2]
    # ********** End **********#

    # 返回df1
    return df1


print(create_dataframe())
