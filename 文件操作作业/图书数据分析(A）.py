import os

file = os.getcwd() + r'/File/CBOOK.csv'

book_ls = []

with open(file, mode='r', encoding='utf8') as fr:
    for line in fr:
        book_ls.append(line.strip().split(','))

n = input()

if n == 'record':
    print(len(book_ls) - 1)
elif n == 'rank':
    k = input()
    for book in book_ls[1:]:
        if book[0] == k:
            print(*book, sep='\n')
            break
elif n == 'maxcomment':
    book_ls = sorted(book_ls[1:], key=lambda x: int(x[5][:-3]), reverse=True)
    for i in range(0, 10):
        print(book_ls[i][1], book_ls[i][-2], sep=' ')
elif n == 'maxname':
    book_ls = sorted(book_ls[1:], key=lambda x: len(x[1]), reverse=True)
    n = int(input())
    for i in range(0, n):
        print(book_ls[i][1])
else:
    print('无数据')
