# -*- coding: utf-8 -*-
import os

import pandas as pd


# 创建透视表,统计顾客在每种用餐时间(time)的小费(tip)总和情况
def create_pivottalbe(data):
    ###### Begin ######
    return data.pivot_table(index='day', columns=['time'], values=['tip'], aggfunc='sum', margins=True)
    ###### End ######


# 创建交叉表,统计顾客在每个星期下(day)的小费(tip)总和情况
def create_crosstab(data):
    ###### Begin ######
    return pd.crosstab(columns=data['time'], index=data['day'], values=data['tip'], aggfunc='sum', margins=True)
    ###### End ######


def main():
    # 读取csv文件数据并赋值给data
    ###### Begin ######
    data = pd.read_csv(os.getcwd() + r'/File/tip.csv', encoding='utf8')
    ###### End ######
    piv_result = create_pivottalbe(data)
    cro_result = create_crosstab(data)
    print("透视表：\n{}".format(piv_result))
    print("交叉表：\n{}".format(cro_result))


if __name__ == '__main__':
    main()
