# -*- coding: utf-8 -*-
"""
了解数据集特征
"""
import os

import pandas as pd

# 1.1 读取Training_Master.csv文件，编码为gbk，命名为master。
############begin############
master = pd.read_csv(os.getcwd() + r'/File/Training_Master.csv', encoding='gbk')

#############end#############

#	1.2 读取Training_Userupdate.csv文件，编码为gbk，命名为user。
############begin############
user = pd.read_csv(os.getcwd() + r'/File/Training_Userupdate.csv', encoding='gbk')

#############end#############

# 1.3 读取Training_LogInfo.csv文件，编码为gbk，命名为log。
############begin############
log = pd.read_csv(os.getcwd() + r'/File/Training_LogInfo.csv', encoding='gbk')

#############end#############

# 1.4 分别输出它们的形状。
############begin############
print(master.shape)
print(user.shape)
print(log.shape)

#############end#############

# 1.5 输出包含master后7个列名的列表。
############begin############
print(master.columns.tolist()[-7:])

#############end#############

# 1.6 输出user表的前3行。
############begin############
print(user.head(3))

#############end#############
