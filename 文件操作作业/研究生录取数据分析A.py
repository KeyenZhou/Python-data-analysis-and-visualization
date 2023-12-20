import os

file = os.getcwd() + r'/File/admit2.csv'

data_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        data_ls.append(line.strip().split(','))

n = input()

if n == '1':
    data_ls = list(filter(lambda x: float(x[-1]) >= 0.8, data_ls[1:]))
    cnt = 0
    for data in data_ls:
        if float(data[1]) >= 4:
            cnt += 1
    print(f'Top University in >=80%:{cnt / len(data_ls):.2%}')
elif n == 'Research':
    data_90 = list(filter(lambda x: float(x[-1]) >= 0.9, data_ls[1:]))
    data_70 = list(filter(lambda x: float(x[-1]) <= 0.7, data_ls[1:]))

    cnt1 = 0
    cnt2 = 0
    for data in data_90:
        if int(data[5]) == 1:
            cnt1 += 1
    for data in data_70:
        if int(data[5]) == 1:
            cnt2 += 1

    print(f'Research in >=90%:{cnt1 / len(data_90) :.2%}')
    print(f'Research in <=70%:{cnt2 / len(data_70) :.2%}')

elif n == '2':
    data_ls = list(filter(lambda x: float(x[-1]) >= 0.8, data_ls[1:]))
    sum_score = 0
    max_score = 0
    min_score = 1e8
    for data in data_ls:
        sum_score += float(data[3])
        max_score = max(max_score, float(data[3]))
        min_score = min(min_score, float(data[3]))
    print(f'TOEFL Average Score:{sum_score / len(data_ls):.2f}')
    print(f'TOEFL Max Score:{max_score:.2f}')
    print(f'TOEFL Min Score:{min_score:.2f}')

elif n == '3':
    data_ls = list(filter(lambda x: float(x[-1]) >= 0.8, data_ls[1:]))
    sum_score = 0
    max_score = 0
    min_score = 1e8
    for data in data_ls:
        sum_score += float(data[4])
        max_score = max(max_score, float(data[4]))
        min_score = min(min_score, float(data[4]))
    print(f'CGPA Average Score:{sum_score / len(data_ls):.3f}')
    print(f'CGPA Max Score:{max_score:.3f}')
    print(f'CGPA Min Score:{min_score:.3f}')

else:
    print('ERROR')
