import os

file = os.getcwd() + r'/File/2019Charity.csv'

data_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        data_ls.append(line.strip().split(','))
n = input()

choose = [str(x) for x in range(1, 101)]

local_list = [x[-3] for x in data_ls[1:]]

local_list = list(set(local_list))

print(local_list)

if n.lower() == 'total'.lower():
    TOTAL = 0
    for data in data_ls[1:]:
        TOTAL += float(data[-1])
    print(f'Total:{TOTAL:.0f}万元')
elif n in choose:
    for data in data_ls[1:]:
        if data[0] == n:
            print(*data)
elif n in local_list:
    for data in data_ls[1:]:
        if data[-3] == n:
            print(*data[0:4])
else:
    print('No Record')
