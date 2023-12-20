import os

file = os.getcwd() + r'/File/university.csv'

school_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        school_ls.append(line.strip().split(','))

name = input()

print(','.join(school_ls[0]))

for school in school_ls[1:]:
    if name == school[1]:
        print(','.join(school), sep='', end='')
