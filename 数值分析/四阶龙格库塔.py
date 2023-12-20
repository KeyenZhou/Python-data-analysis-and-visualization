#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 22:54
# @Author  : Sundy_Loly
# @File    : 四阶龙格库塔.py
# @Software: PyCharm
import numpy
import matplotlib.pyplot as plt


def f(x, y):
    return y - 2 * x / y


h = 0.2

x_array = numpy.arange(0, 2, h)

y_xn = (1 + 2 * x_array) ** (1 / 2)

y_long = [1]

for i in range(1, len(x_array)):
    x0 = x_array[i - 1]
    y0 = y_long[i - 1]
    x1 = x_array[i]
    k1 = f(x0, y0)
    k2 = f(x0 + h / 2, y0 + h / 2 * k1)
    k3 = f(x0 + h / 2, y0 + h / 2 * k2)
    k4 = f(x0 + h, y0 + h * k3)
    y_long.append(y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

plt.plot(x_array, y_xn, marker='^')

plt.plot(x_array, y_long, marker='v')

plt.show()
