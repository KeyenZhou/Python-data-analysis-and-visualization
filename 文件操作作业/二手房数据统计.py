import os

file = os.getcwd() + r'/File/house.csv'

data_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        data_ls.append(line.strip().split(','))

n = input()

if n == '最高总价':
    k = int(input())
    head_ls = data_ls[0]
    data_ls = sorted(data_ls[1:], key=(lambda x: float(x[8])), reverse=True)
    print(*head_ls)
    for i in range(0, k):
        print(*data_ls[i])
elif n == '最大面积':
    k = int(input())
    head_ls = data_ls[0]
    data_ls = sorted(data_ls[1:], key=(lambda x: float(x[7])), reverse=True)
    print(*head_ls)
    for i in range(0, k):
        print(*data_ls[i])
elif n == '最高单价':
    head_ls = data_ls[0]
    data_ls = sorted(data_ls[1:], key=(lambda x: float(x[8]) / float(x[7])), reverse=True)
    print(*head_ls)
    print(*data_ls[0])
elif n == '精装电梯房单价':
    data_ls = list(filter(lambda x: x[6] == '有电梯' and x[5] == '精装', data_ls[1:]))
    data_ls = sorted(data_ls, key=lambda x: float(x[8]))
    sum_price = 0.0
    sum_area = 0.0
    for data in data_ls:
        sum_price += float(data[8])
        sum_area += float(data[7])
    print('{:.2f}万元'.format(sum_price / sum_area))
elif n == '房屋朝向':
    s = input()
    cnt = 0
    for data in data_ls[1:]:
        if data[3] == s:
            cnt += 1
    if cnt != 0:
        print(f'{cnt}套')
    else:
        print('无数据')
else:
    print(*data_ls[0])
    flag = False
    for data in data_ls[1:]:
        if n in data[1]:
            print(*data)
            flag = True

    if not flag:
        print('未找到相关数据')
