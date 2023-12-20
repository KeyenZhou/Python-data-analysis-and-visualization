import numpy as np

n = input().lower()

if n == 'array':
    data_ls = eval(input())
    data_array = np.array(data_ls)
    print(data_array)
elif n == 'arange':
    start, stop, step = tuple(map(int, input().strip().split(' ')))
    print(np.arange(start, stop, step))
elif n == 'linspace':
    start, stop, num = tuple(map(int, input().strip().split(' ')))
    print(np.linspace(start, stop, num))
elif n == 'logspace':
    start, stop, num, base = tuple(map(int, input().strip().split(' ')))
    print(np.logspace(start, stop - 1, num=num, base=base))
elif n == 'zeros':
    a, b = tuple(map(int, input().strip().split(' ')))
    print(np.zeros((a, b)))
elif n == 'ones':
    a, b = tuple(map(int, input().strip().split(' ')))
    print(np.ones((a, b)))
elif n == 'full':
    a, b, c = tuple(map(int, input().strip().split(' ')))
    print(np.full((a, b), c))
elif n == 'identity':
    a, = tuple(map(int, input().strip().split(' ')))
    print(np.identity(a))
elif n == 'randint':
    a, b, c, d, e = tuple(map(int, input().strip().split(' ')))
    np.random.seed(a)
    print(np.random.randint(b, c, (d, e)))
else:
    print('ERROR')
