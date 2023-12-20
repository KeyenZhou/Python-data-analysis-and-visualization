#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 16:14
# @Author  : Sundy_Loly
# @File    : 数值积分与微分.py
# @Software: PyCharm

import math


def f(x: float):
    return 1 / x


def get_new_T(old: float, h_: float, n_: int, a_: float):
    sum_ = 0
    for i_ in range(n_):
        sum_ += f(a_ + (i_ + 0.5) * h_)
    return old / 2 + h_ / 2 * sum_


a = 1
b = 5
T = (b - a) / 2 * (f(a) + f(b))
h = b - a
n = 1

T_ls = []

for i in range(3):
    T_ls.append(T)
    new_T = get_new_T(T, h, n, a)
    T = new_T
    n *= 2
    h /= 2

T_ls.append(T)

S_ls = [(4 * y - x) / 3 for x, y in zip(T_ls[:-1], T_ls[1:])]

C_ls = [(16 * y - x) / 15 for x, y in zip(S_ls[:-1], S_ls[1:])]

R_ls = [(64 * y - x) / 63 for x, y in zip(C_ls[:-1], C_ls[1:])]

print(R_ls)
