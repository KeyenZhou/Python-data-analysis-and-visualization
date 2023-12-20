import os

file = os.getcwd() + r'/File/成绩单.csv'

n = int(input())

data_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        data_ls.append(line.strip().split(','))

data_ls = sorted(data_ls, key=lambda x: int(x[-1]))

fr_n = []
la_n = []

n = min(n, len(data_ls))

for i in range(0, n):
    fr_n.append(data_ls[i])
    la_n.append((data_ls[i - n]))

print(f'最低分{data_ls[0][-1]}分,最高分{data_ls[-1][-1]}分')

print(fr_n)
print(la_n)

average_sum = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for data in data_ls:
    for i in range(3, 9):
        average_sum[i - 3] += float(data[i])

ans = [round(i / len(data_ls), 2) for i in average_sum]

print(ans)
