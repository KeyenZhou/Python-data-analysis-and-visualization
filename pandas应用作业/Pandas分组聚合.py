import os

import pandas as pd
import numpy as np

'''
返回df中最大值与最小值的差
'''
file = os.getcwd() + r'/File/drinks.csv'


def sub(df):
    ######## Begin #######
    return df.max() - df.min()

    ######## End #######


'''
利用groupby、agg、统计函数和自定义函数sub，求每个大洲红酒消耗量的最大值与最小值的差以及啤酒消耗量的和
'''


def main():
    ######## Begin #######
    drinks = pd.read_csv(file, encoding='utf8', index_col=0)
    # print(drinks.columns)
    # print(drinks.index)
    mapping = {
        'wine_servings': sub,
        'beer_servings': np.sum
    }
    drinks_grouped = drinks.groupby(by=drinks['continent'])
    print(drinks_grouped.agg(mapping))

    # for key, item in drinks_grouped:
    #     min_ = item['wine_servings'].min()
    #     max_ = item['wine_servings'].max()
    #     print(max_ - min_)
    #     sum_ = item['beer_servings'].sum()
    #     print(sum_)
    ######## End #######


if __name__ == '__main__':
    main()
