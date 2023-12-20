#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 10:30
# @Author  : Sundy_Loly
# @File    : 二分法.py
# @Software: PyCharm
import math


def f(x):
    return x ** 3 - x - 1


# f(1) = -1
# f(2) = 5


eps = 1e-10

L = 1.0
R = 2.0

while math.fabs(R - L) > eps:
    mid = (L + R) / 2
    if f(mid) > 0:
        R = mid
    else:
        L = mid

print(L)
