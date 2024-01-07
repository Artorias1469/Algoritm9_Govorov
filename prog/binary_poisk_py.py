#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import matplotlib.pyplot as plt
import sympy as sp
import math
import bisect


def binary_poisk(nums, target):
    return bisect.bisect_left(nums, target)


def roots(x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x2 = sum(i**2 for i in x)
    sum_xy = sum([i * j for i, j in zip(x, y)])

    n = len(x) + 1

    a, b = sp.symbols('a b')

    equation_1 = sp.Eq(sum_x2 * a + sum_x * b, sum_xy)
    equation_2 = sp.Eq(sum_x * a + (n) * b, sum_y)

    sol = sp.solve((equation_1, equation_2), (a, b))

    x1 = x
    x2 = [sol[a] * math.log(i, 2) + sol[b] for i in x1]
    return x1, x2


def create_grf(x, y, x1, y1, name_of_graph, name_x, name_y):
    plt.plot(x, y, 'o', color='red')
    plt.plot(x1, y1, '.-', color='black')

    plt.xlabel(name_x)
    plt.ylabel(name_y)

    plt.title(name_of_graph)
    plt.show()
    

def binary_poisk_grf(x=[], y=[]):
    for i in range(1000, 50001, 1000):
        x.append(i)
        nums = [j for j in range(i)]
        execution_time = timeit.timeit(
            lambda: binary_poisk(nums, nums[-1]), number=1
        )/6
        y.append(execution_time)
    
    x1, y1 = roots(x, y)

    create_grf(
        x,
        y,
        x1,
        y1, 
        "Бинарный поиск", 
        "Размер", 
        "Время"
    )


if __name__ == '__main__':
    binary_poisk_grf()