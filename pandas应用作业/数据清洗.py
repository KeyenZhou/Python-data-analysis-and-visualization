# -*- coding: utf-8 -*-
"""
数据清洗
"""
import os

import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

ChinaData = pd.read_csv(os.getcwd() + r'/File/ChinaData.csv', index_col=0)
'''
请针对ChinaData完成如下操作。
'''
# 2.1 按如下格式输出删除前ChinaData的形状
# 格式：原表形状(x, y)
############begin############
print(f'原表形状{ChinaData.shape}')
row_origin = ChinaData.shape[0]

#############end#############

# 2.2 直接删除ChinaData的空白行
# 提示：dropna,inplace
############begin############
ChinaData.dropna(how='all', inplace=True)

#############end#############

# 2.3 按如下格式输出删除后ChinaData的形状
# 格式：新表形状(x, y)
############begin############
print(f'新表形状{ChinaData.shape}')
row_new = ChinaData.shape[0]

#############end#############

# 2.4 按如下格式输出被删除的空行数
# 格式：XX个空白行被删除。
############begin############
print(f'{row_origin - row_new}个空白行被删除。')

#############end#############

# 2.5 查找数据最完整（空值最少）的年份并输出
# 提示：notnull(),根据值找索引
############begin############
my_null = []
for col in ChinaData.columns:
    null_ = ChinaData[col].isnull().sum()
    my_null.append([col, null_])

min_ = min(my_null, key=lambda x: x[1])

print(min_[0])

#############end#############

# 2.6 前向填充"男性吸烟率（吸烟男性占所有成年人比例）"，输出2000年至2019年的数据
# fillna,ffill
############begin############
ChinaData.loc["男性吸烟率（吸烟男性占所有成年人比例）", :].fillna(method='pad', inplace=True, axis=0)
print(ChinaData.loc["男性吸烟率（吸烟男性占所有成年人比例）", [str(x) for x in range(2000, 2020)]])

#############end#############
