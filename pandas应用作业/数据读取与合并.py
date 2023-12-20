# -*- coding: utf-8 -*-
import os

import pandas as pd

"""
数据读取与合并
现有源自世界银行的四个数据集(编码均为UTF-8)：
1)economy-60-78.csv，
2)economy-79-19.csv，
3)population-60-78.csv，
4)population-79-19.csv，
其中分别存放了不同时间段（1960-1978和1979-2019）的
中国经济相关数据和中国人口及教育相关数据。
"""
# 请将上述数据集内容读取至DataFrame结构中，
# 年份为列索引，Indicator Name为行索引，
# 观察其结构和内容，把它们合并为一个DataFrame。
# 先按年份顺序沿着轴1拼接economy-60-78和economy-79-19；
# 再按年份顺序沿着轴1拼接population-60-78和population-79-19；
# 最后沿着轴0将前两次的拼接的结果拼接起来，命名为ChinaData
# 输出ChinaData的形状
############begin############
economy_60_78 = pd.read_csv(os.getcwd() + r'/File/economy-60-78.csv', encoding='utf8', index_col=0)
economy_79_19 = pd.read_csv(os.getcwd() + r'/File/economy-79-19.csv', encoding='utf8', index_col=0)
population_60_78 = pd.read_csv(os.getcwd() + r'/File/population-60-78.csv', encoding='utf8', index_col=0)
population_79_19 = pd.read_csv(os.getcwd() + r'/File/population-79-19.csv', encoding='utf8', index_col=0)

economy_60_19 = pd.concat([economy_60_78, economy_79_19], axis=1, join='outer', sort=True)
population_60_19 = pd.concat([population_79_19, population_60_78], axis=1, join='outer', sort=True)

ChinaData = pd.concat([economy_60_19, population_60_19], axis=0, join='outer', sort=True)

print(ChinaData.shape)

#############end#############
