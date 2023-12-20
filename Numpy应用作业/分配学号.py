import os

file1 = os.getcwd() + r'/File/studentList.csv'

file2 = os.getcwd() + r'/File/schoolCode.csv'

file3 = os.getcwd() + r'/File/MajorCode.csv'

student_ls = []

schoolCode_ls = []

majorCode_ls = []

with open(file1, mode='r', encoding='utf8') as fr:
    for line in fr:
        student_ls.append(line.strip().split(','))

with open(file2, mode='r', encoding='utf8') as fr:
    for line in fr:
        schoolCode_ls.append(line.strip().split(','))

with open(file3, mode='r', encoding='utf8') as fr:
    for line in fr:
        majorCode_ls.append(line.strip().split(','))

schoolCode_ls = [tuple(x) for x in schoolCode_ls]

schoolCode_dict = {item[0]: item[1] for item in schoolCode_ls}

majorCode_dict = {item[0]: item[1] for item in majorCode_ls}

name = input()

xuehao = ''
banji = ''
student_na = []

for student in student_ls:
    if student[0] == name:
        xuehao = '012' + student[-1][-2:] + schoolCode_dict[student[2]] + majorCode_dict[student[3]] + student[-2][-4:]
        banji = student[-2]
        student_na = student
        break

cnt = 0

for student in student_ls:
    if student[-2] == banji:
        cnt += 1
        if student[0] == name:
            break

xuehao += str(cnt).zfill(2)

print(xuehao, *student_na)

banji_in = input()

student_ls = list(filter(lambda x: x[-2] == banji_in, student_ls))

for i in range(0, len(student_ls)):
    xuehao = '012' + student_ls[i][-1][-2:] + schoolCode_dict[student_ls[i][2]] + majorCode_dict[student_ls[i][3]] + \
             student_ls[i][-2][-4:] + str(i + 1).zfill(2)
    print(xuehao, *student_ls[i])
