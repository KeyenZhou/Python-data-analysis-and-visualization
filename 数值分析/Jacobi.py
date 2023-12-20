#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 10:48
# @Author  : Sundy_Loly
# @File    : Jacobi.py
# @Software: PyCharm

import math

import numpy as np

A = [[10, -1, -2], [-1, 10, -2], [-1, -1, 5]]

b = [[7.2], [8.3], [4.2]]

tol = 1e-5

x = [0, 0, 0]

y = [0, 0, 0]

A_ = A.copy()

np.set_printoptions(formatter={'float': '{:10.8f}'.format})

for i in range(20):
    for j in range(len(A)):
        sum_ = 0
        for z in range(len(A)):
            if z == j:
                continue
            sum_ += A[j][z] * x[z]
        y[j] = b[j][0] / A[j][j] - sum_ / A[j][j]

    z = [math.fabs(z[0] - z[1]) for z in zip(x, y)]

    if max(z) < tol:
        print(y)
        break

    x = y.copy()
