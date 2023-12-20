import os
import numpy as np

file = os.getcwd() + r'/File/iris_sepal_length.csv'

data_array = np.loadtxt(file, dtype=float, encoding='utf8')

unique = np.unique(data_array)

sort_array = np.sort(unique, kind='stable')

n = int(input())

ans_array = sort_array[:n]

print(f'''花萼长度的最大值是：{np.max(ans_array):.2f}
花萼长度的最小值是：{np.min(ans_array):.2f}
花萼长度的均值是：{np.average(ans_array):.2f}
花萼长度的方差是：{np.var(ans_array):.2f}
花萼长度的标准差是：{np.std(ans_array, ddof=1):.2f}''')  # ddof=0计算总体标准差 ddof=1计算样本标准差
