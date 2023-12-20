#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 22:19
# @Author  : Sundy_Loly
# @File    : 欧拉法.py
# @Software: PyCharm

import numpy
import matplotlib.pyplot as plt

# x0, y0, h, n = list(map(eval, input().strip().split()))

x0 = 0
h = 0.2
y1 = 1


def f(x, y):
    return y - 2 * x / y


x = numpy.arange(0, 2, h)

# print(x)

y_xn = (1 + 2 * x) ** 1.2

y_ls = [1]

y_ga = [1]

plt.plot(x, y_xn)

for i in range(1, len(x)):
    yi = y_ls[i - 1] + h * f(x[i - 1], y_ls[i - 1])
    y_ls.append(yi)
    plt.plot([x[i - 1], x[i]], [y_ls[i - 1], y_ls[i]])

for i in range(1, len(x)):
    yp = y_ga[i - 1] + h * f(x[i - 1], y_ga[i - 1])
    yc = y_ga[i - 1] + h * f(x[i], yp)
    y_ga.append((yp + yc) / 2)

print(y_ls)
print(y_xn)
print(y_ga)

plt.plot(x, y_ga)

plt.show()
