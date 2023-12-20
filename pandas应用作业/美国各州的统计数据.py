import os

import pandas as pd
import numpy as np


def task3():
    # ********** Begin **********#
    # 读取三个csv文件
    state_areas = pd.read_csv(os.getcwd() + r'/File/state-areas.csv')
    state_abbrevs = pd.read_csv(os.getcwd() + r'/File/state-abbrevs.csv')
    state_population = pd.read_csv(os.getcwd() + r'/File/state-population.csv')
    # 合并pop和abbrevs并删除重复列
    ans = pd.merge(state_population, state_abbrevs, left_on='state/region', right_on='abbreviation', how='outer')
    # ans.drop_duplicates()
    ans = ans.drop('abbreviation', axis=1)
    # print(ans)
    # print(ans)
    # 填充对应的全称
    ans.loc[ans['state/region'] == 'PR', 'state'] = 'Puerto Rico'
    ans.loc[ans['state/region'] == 'USA', 'state'] = 'United States'
    # print(ans)
    # 合并面积数据
    merged = pd.merge(state_areas, ans, left_on='state', right_on='state', how='outer')
    # 删掉这些缺失值
    merged.dropna(inplace=True)
    # print(merged)
    # 取year为2010年的数据，并将索引设为state列
    year_2010_under18 = merged.query('year==2010 & ages == "under18"')
    year_2010_total = merged.query('year == 2010 & ages =="total"')
    pop_sum = np.array(year_2010_under18.loc[:, 'population']) + np.array(year_2010_total.loc[:, 'population'])
    res = year_2010_total.copy()
    # print(res)
    res.loc[:, 'population'] = pop_sum
    # print(res)
    # 计算人口密度
    res.set_index('state', inplace=True)
    # print(res)
    midu = res.loc[:, 'population'] / res.loc[:, 'area (sq. mi)']
    # # 对密度求和
    sum_ = np.sum(midu)
    # 对值进行排序
    midu.sort_values(inplace=True, ascending=False)
    # print(res)
    # 输出人口密度前5名和倒数5名
    print('前5名：')
    print(midu.head())
    print('后5名：')
    print(midu.tail())


# print(res.loc[:, ['state', 'midu']].tail())
# ********** End **********#

if __name__ == '__main__':
    task3()
