# -*- coding: utf-8 -*-
"""
DataFrame的CRUD
"""
import pandas as pd

master = pd.read_csv("File/Training_Master.csv", encoding='gbk')
user = pd.read_csv("File/Training_Userupdate.csv", encoding='gbk')
log = pd.read_csv("File/Training_LogInfo.csv", encoding='gbk')

#	2.1 求取master表的列名前缀列表，并按字母升序输出该列表。
#     例如：SocialNetwork_12列的列名前缀为：SocialNetwork
############begin############
master_columns = sorted(list(set([x.split('_')[0] for x in master.columns.tolist()])))
print(master_columns)
# type(master['UserInfo_1'])
#############end#############

#	2.2 删除master中列名前缀为：SocialNetwork的列
#     输出：共**列被删除。
############begin############
master_column = master.columns
cnt = 0
for name in master_column:
    if 'SocialNetwork' in name:
        master.drop(name, axis=1)
        cnt += 1
print(f'共{cnt}列被删除。')

#############end#############

#	2.3在master表最右侧增加一列Result，
#    记录UserInfo_1和UserInfo_3的和，
#    并输出这三列的前5行。
############begin############

# list_ans = []
#
user1 = master.loc[:, 'UserInfo_1']
user3 = master['UserInfo_3']

result = user1 + user3

master['Result'] = result

print(master.loc[:, ['UserInfo_1', 'UserInfo_3', 'Result']].head(5))

#############end#############

#	2.4将UserInfo_2列中所有的“深圳”替换为“中国深圳”，
#    并计算“中国深圳”的用户数。
############begin############
master['UserInfo_2'].replace('深圳', '中国深圳', inplace=True)
print(master.UserInfo_2.value_counts()['中国深圳'])
#############end#############
