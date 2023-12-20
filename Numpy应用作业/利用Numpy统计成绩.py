import os
import numpy as np

file = os.getcwd() + r'\File\成绩单数字.csv'

data_array = np.loadtxt(file, dtype=str, delimiter=',', encoding='utf8')

scoreNum = data_array[1:, 2:].astype(int)

list_head = list(*data_array[:1].tolist())

list_left = list(*data_array[1:, :1].reshape(1, 5).tolist())

name = input()

major = input()

name_index = list_left.index(name)

print(f'{name}同学的总分为{np.sum(scoreNum[name_index]):.2f}')

print(f'{name}同学的平均分为{np.mean(scoreNum[name_index]):.2f}')

major_index = list_head.index(major) - 2

print(f'{major}课程平均成绩为{np.mean(scoreNum[:, major_index]):.2f}')

print(f'{major}课程中位数为{np.median(scoreNum[:, major_index]):.2f}')

print(f'{major}课程标准差为{np.std(scoreNum[:, major_index]):.2f}')
