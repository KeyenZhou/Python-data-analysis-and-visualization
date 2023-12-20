#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 11:10
# @Author  : Sundy_Loly
# @File    : Gauss-Seidel.py
# @Software: PyCharm
import numpy as np

A = np.array([[10, -1, -2], [-1, 10, -2], [-1, -1, 5]], dtype='float')

b = np.array([[7.2], [8.3], [4.2]], dtype='float')

tol = 1e-5

N = 100

x = np.array([[0], [0], [0]], dtype='float')

x_backup = x.copy()

y = np.array([[0], [0], [0]], dtype='float')

A_ = A.copy()

for i in range(0, len(A)):
    A_[i, i] = 0

flag = True

np.set_printoptions(formatter={'float': '{:10.8f}'.format})

for i in range(N):
    for j in range(len(A)):
        # y[j, 0] = np.mat(b[j] - np.dot(A_[j, :], x), A[j, j])
        y[j, 0] = (b[j] - A_[j, :] @ x) / A[j, j]
        x_backup[j] = x[j]
        x[j] = y[j]

    if np.max(np.fabs(x_backup - y)) < tol:
        print(f"迭代次数 {i}")
        print(f"方程组的根 {y}")
        flag = False
        break

if flag:
    print("迭代方法失败")
