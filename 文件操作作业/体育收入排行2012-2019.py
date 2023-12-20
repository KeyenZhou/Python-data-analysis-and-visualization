import os
import re

file = os.getcwd() + r'/File/2012-19sport.csv'

data_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        data_ls.append(line.strip().split(','))

n = input()

year_ls = [str(x) for x in range(2012, 2020)]

if n in year_ls:
    k = int(input())
    data_ls = list(filter(lambda x: x[-1] == n, data_ls[1:]))
    for i in range(0, min(len(data_ls), k)):
        s = ' | '.join(data_ls[i])
        if s[0] != '#':
            print(s)
        else:
            print(s[1:])

elif n.lower() == 'SPORT'.lower():
    year = input()
    game = []
    data_ls = list(filter(lambda x: x[-1] == year, data_ls[1:]))
    for data in data_ls:
        if data[-2] not in game:
            game.append(data[-2])

    game = sorted(game)

    for i in range(0, len(game)):
        print(f'{i + 1}: {game[i]}')

    k = int(input())

    data_ls = list(filter(lambda x: x[-2] == game[k - 1], data_ls))

    Total = 0

    for data in data_ls:
        s = ' | '.join(data)
        p = re.compile(r'[^$\sM]+')
        Total += float(p.findall(data[2])[0])
        print(s[1:])

    print(f' TOTAL:${Total:.2f} M')
else:
    print('Wrong Input')
