#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 14:27
# @Author  : Sundy_Loly
# @File    : 插值方法.py
# @Software: PyCharm

import numpy as np


# 拉格朗日插值
def f_la(x: np.ndarray, k: int, x0: float) -> float:
    f = 1
    for i in range(0, len(x)):
        if i != k:
            f *= (x0 - x[i]) / (x[k] - x[i])
    return f


def f_la_ans(x: np.ndarray, y: np.ndarray, x0: float) -> float:
    f = 0
    for i in range(0, len(x)):
        f += y[i] * f_la(x, i, x0)
    return f


def test01():
    x_get = np.array([0.4, 0.5, 0.6, 0.7, 0.8])

    y_get = np.array([-0.9163, -0.6931, -0.5108, -0.3567, -0.2231])

    print(f_la_ans(x_get, y_get, 0.54))


# newton 插值

# 初始化基底
def get_new_w(x: np.ndarray, x0: float) -> np.ndarray:
    ans = []
    value = 1
    ans.append(1)
    for xi in x:
        value *= (x0 - xi)
        ans.append(value)

    return np.array(ans)


# 增加新的插值节点后
def get_add(x: np.ndarray, xi: float, x0: float) -> np.ndarray:
    new_x = np.append(x, x[-1] * (x0 - xi))
    return new_x


def get_poor(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    ans = np.zeros((len(x), len(x) + 2))
    ans[:, 0] = x
    ans[:, 1] = y
    for i in range(1, len(x)):
        for j in range(2, i + 2):
            ans[i, j] = (ans[i, j - 1] - ans[i - 1, j - 1]) / (ans[i, 0] - ans[i - (j - 1), 0])
    return np.diag(ans[:, 1:])


def f_new(w: np.ndarray, poor: np.ndarray) -> float:
    f = 0
    for i, j in zip(w, poor):
        f += i * j

    return f


def test02():
    x_get = np.array([0.4, 0.5, 0.6, 0.7, 0.8])

    y_get = np.array([-0.9163, -0.6931, -0.5108, -0.3567, -0.2231])

    w = get_new_w(x_get, 0.54)

    poor = get_poor(x_get, y_get)

    print(f_new(w, poor))


def test03():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    xy = 0
    xx = 0
    yy = 0
    xxx = 0
    for i in range(5):
        xy += x[i] * y[i]
        xx += x[i]
        yy += y[i]
        xxx += x[i] * x[i]

    k = (xy - xx * yy / 5) / (xxx - xx / 5)

    b = yy / 5 - k * xx / 5

    print(k, b)


if __name__ == '__main__':
    test01()
    test02()
    test03()
