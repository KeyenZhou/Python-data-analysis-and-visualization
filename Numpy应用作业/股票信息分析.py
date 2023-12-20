import os
import numpy as np

file = os.getcwd() + r'/File/China Minsheng Bank.csv'

data_array = np.loadtxt(file, dtype=str, delimiter=',', encoding='utf8')

data_ls = data_array.tolist()

choose = input()

if choose == '最高价':
    n = int(input())
    data_ls = sorted(data_ls[1:], key=lambda x: float(x[4]), reverse=True)
    print(f'最高价从高到低前{n}名:')
    for i in range(0, n):
        print(f'{data_ls[i][0]} {data_ls[i][4]}元')
elif choose == '开盘价':
    n = int(input())
    data_ls = sorted(data_ls[1:], key=lambda x: float(x[6]))
    print(f'开盘价从低到高前{n}名:')
    for i in range(0, n):
        print(f'{data_ls[i][0]} {data_ls[i][6]}元')
elif choose == '成交金额':
    n = int(input())
    data_ls = sorted(data_ls[1:], key=lambda x: float(x[-1]), reverse=True)
    money_sum = 0
    for i in range(0, n):
        money_sum += float(data_ls[i][-1])

    print(f'成交金额最多的{n}天成交额为{money_sum:.0f}元')
elif choose == '日期':
    date = input()
    for data in data_ls[1:]:
        if data[0] == date:
            print(*data)
