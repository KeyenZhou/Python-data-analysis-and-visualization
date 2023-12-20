#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 10:39
# @Author  : Sundy_Loly
# @File    : 牛顿迭代法.py
# @Software: PyCharm
import math
from math import exp

eps = 1e-5

N = 100

x0 = 0.5


def f(x):
    return x - (x - exp(-x)) / (1 + x)


flag = True

for i in range(N):
    x1 = f(x0)
    if math.fabs(x1 - x0) < eps:
        print("方程正根" + str(x1))
        flag = False
        break

    x0 = x1
if flag:
    print("迭代失败")
